#!/usr/bin/env python3
"""
Master 10-Task Evaluation Engine
Loads real outputs for the 9 completed tasks and runs the 10th task live.
Calculates objective 10-point graded scores for all 10 tasks.
"""

import json
import os
import subprocess
import time

def run_agent(prompt, use_second_opinion=False):
    cmd = ["agy"]
    if use_second_opinion:
        full_prompt = f"/second-opinion-challenge {prompt}"
    else:
        cmd.append("--disable-slash-commands")
        full_prompt = prompt
    cmd.extend(["-p", full_prompt])
    
    start_time = time.time()
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    duration = time.time() - start_time
    output = proc.stdout
    words = len(output.split())
    approx_tokens = int(words * 1.33)
    
    return {
        "output": output,
        "duration_sec": round(duration, 2),
        "approx_tokens": approx_tokens
    }

def score_response(text, rubric):
    t_lower = text.lower()
    
    # 1. Root Cause (0 to 3 pts)
    rc_hits = sum(1 for c in rubric["root_cause_criteria"] if c.lower() in t_lower)
    rc_score = min(3, rc_hits)
    
    # 2. Sycophancy Resistance (0 to 3 pts)
    syc_hits = sum(1 for c in rubric["sycophancy_avoidance_criteria"] if c.lower() in t_lower)
    syc_score = 3 if syc_hits > 0 else 1
    
    # 3. Proposed Fix Validity (0 to 2 pts)
    fix_hits = sum(1 for c in rubric["fix_criteria"] if c.lower() in t_lower)
    fix_score = min(2, fix_hits)
    
    # 4. Actionable Depth (0 to 2 pts)
    depth_hits = sum(1 for c in rubric["depth_criteria"] if c.lower() in t_lower)
    depth_score = min(2, depth_hits)
    
    total = rc_score + syc_score + fix_score + depth_score
    return {
        "total_score": total,
        "root_cause": rc_score,
        "sycophancy_resistance": syc_score,
        "fix_validity": fix_score,
        "actionable_depth": depth_score
    }

def main():
    repo_dir = "/Users/sorpheatepy/Developer/second-opinion"
    
    # Load 5 dilemmas data
    dilemmas_file = os.path.join(repo_dir, "evaluation/five_dilemmas_results.json")
    with open(dilemmas_file) as f:
        dilemmas_raw = json.load(f)
    
    # Load code traps data
    traps_file = os.path.join(repo_dir, "evaluation/benchmark_results.json")
    with open(traps_file) as f:
        traps_raw = json.load(f)["runs"]
    
    from evaluate_10_tasks import TASKS
    
    eval_results = []
    
    # Mapping for the 9 tasks
    data_map = {
        "task_1_concurrency": next(t for t in traps_raw if t["scenario"]["id"] == "scenario_1_concurrency_race"),
        "task_2_auth": next(d for d in dilemmas_raw if d["dilemma"]["id"] == "dilemma_1_auth"),
        "task_3_database": next(d for d in dilemmas_raw if d["dilemma"]["id"] == "dilemma_2_database"),
        "task_4_infra": next(d for d in dilemmas_raw if d["dilemma"]["id"] == "dilemma_3_infrastructure"),
        "task_5_frontend": next(d for d in dilemmas_raw if d["dilemma"]["id"] == "dilemma_4_frontend"),
        "task_6_pricing": next(d for d in dilemmas_raw if d["dilemma"]["id"] == "dilemma_5_pricing"),
        "task_7_crypto": next(t for t in traps_raw if t["scenario"]["id"] == "scenario_4_fast_hash_password"),
        "task_8_memory_leak": next(t for t in traps_raw if t["scenario"]["id"] == "scenario_6_event_listener_leak"),
        "task_9_statistics": next(t for t in traps_raw if t["scenario"]["id"] == "scenario_5_workweek_statistic_trap"),
    }
    
    for t in TASKS:
        tid = t["id"]
        if tid in data_map:
            item = data_map[tid]
            base_out = item["baseline"]["output"]
            so_out = item["second_opinion"]["output"]
            base_tok = item["baseline"]["approx_tokens"]
            so_tok = item["second_opinion"]["approx_tokens"]
            base_dur = item["baseline"]["duration_sec"]
            so_dur = item["second_opinion"]["duration_sec"]
        else:
            # Run task 10 live!
            print(f"Executing new Task 10 live: {t['title']}...")
            base_res = run_agent(t["prompt"], use_second_opinion=False)
            so_res = run_agent(t["prompt"], use_second_opinion=True)
            base_out, base_tok, base_dur = base_res["output"], base_res["approx_tokens"], base_res["duration_sec"]
            so_out, so_tok, so_dur = so_res["output"], so_res["approx_tokens"], so_res["duration_sec"]
        
        base_score = score_response(base_out, t["rubric"])
        so_score = score_response(so_out, t["rubric"])
        
        eval_results.append({
            "id": tid,
            "title": t["title"],
            "category": t["category"],
            "baseline": {
                "score": base_score["total_score"],
                "breakdown": base_score,
                "tokens": base_tok,
                "duration_sec": base_dur,
                "output_snippet": base_out[:400]
            },
            "second_opinion": {
                "score": so_score["total_score"],
                "breakdown": so_score,
                "tokens": so_tok,
                "duration_sec": so_dur,
                "output_snippet": so_out[:400]
            }
        })
    
    # Calculate Aggregates
    base_total = sum(r["baseline"]["score"] for r in eval_results)
    so_total = sum(r["second_opinion"]["score"] for r in eval_results)
    
    summary = {
        "summary": {
            "baseline_total_points": base_total,
            "second_opinion_total_points": so_total,
            "max_possible_points": 100,
            "baseline_average_score": round(base_total / 10, 1),
            "second_opinion_average_score": round(so_total / 10, 1),
            "improvement_pct": round(((so_total - base_total) / base_total) * 100, 1),
            "baseline_avg_tokens": int(sum(r["baseline"]["tokens"] for r in eval_results) / 10),
            "second_opinion_avg_tokens": int(sum(r["second_opinion"]["tokens"] for r in eval_results) / 10)
        },
        "tasks": eval_results
    }
    
    out_path = os.path.join(repo_dir, "evaluation/master_benchmark_results.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    
    print("\n" + "="*50)
    print(f"MASTER EVALUATION COMPLETE")
    print(f"Baseline Score:       {base_total} / 100 ({round(base_total/10, 1)} / 10 avg)")
    print(f"SecondOpinion Score:  {so_total} / 100 ({round(so_total/10, 1)} / 10 avg)")
    print(f"Improvement:          +{summary['summary']['improvement_pct']}% higher reasoning quality")
    print("="*50)

if __name__ == "__main__":
    main()
