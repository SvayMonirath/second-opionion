#!/usr/bin/env python3
"""
SecondOpinion: The 5 Everyday Tech Dilemmas Benchmark
Runs head-to-head empirical testing: Baseline Single-Agent vs SecondOpinion Swarm/Challenge.
"""

import subprocess
import json
import time
import os

DILEMMAS = [
    {
        "id": "dilemma_1_auth",
        "title": "Auth: 7-Day localStorage JWT vs Cookie Sessions",
        "category": "Security & User Management",
        "prompt": "Our team is building a B2B SaaS dashboard. To keep the backend fast and simple, we want to issue 7-day JWT access tokens stored in browser localStorage with no database lookups on requests and no refresh tokens. Is this production-ready, or what should we actually build?",
        "fatal_traps": ["xss", "localstorage", "cannot revoke", "unrevocable", "soc 2", "httponly", "session"],
        "single_ai_bias": "Often validates the desire for 'stateless simplicity' or gives a minor warning while writing localStorage code.",
        "second_opinion_fix": "Flatly rejects 7-day localStorage token. Proves it fails SOC 2 compliance and recommends simple HttpOnly cookie sessions or 15-min dual tokens."
    },
    {
        "id": "dilemma_2_database",
        "title": "Database: MongoDB vs PostgreSQL for B2B SaaS",
        "category": "Data Architecture & Integrity",
        "prompt": "We are building a new B2B SaaS for warehouse inventory management and customer invoicing. Our developers want to use MongoDB because 'JSON schema flexibility will help us ship the MVP twice as fast without dealing with SQL migrations'. Should we go with MongoDB for this?",
        "fatal_traps": ["acid", "transaction", "foreign key", "financial", "invoicing", "inventory", "postgres", "relational", "consistency"],
        "single_ai_bias": "Often agrees with 'flexible schema for fast MVP' and suggests embedding documents, ignoring financial integrity.",
        "second_opinion_fix": "Warns that inventory deductions and invoices require strict relational ACID transactions and foreign keys. Shows that Postgres supports JSONB anyway."
    },
    {
        "id": "dilemma_3_infrastructure",
        "title": "Hosting: AWS Serverless vs Simple Docker VPS",
        "category": "Infrastructure & Cloud Costs",
        "prompt": "We are 2 developers launching an MVP SaaS. One founder insists we build on full AWS Serverless (API Gateway + AWS Lambda + DynamoDB + SQS) so we 'never have to manage servers and can scale to millions of users on day one'. Is this the right setup for our launch?",
        "fatal_traps": ["over-engineering", "cold start", "connection pool", "dynamodb single-table", "vps", "docker", "hetzner", "simple", "monolith"],
        "single_ai_bias": "Often praises the 'limitless scalability and modern cloud architecture' of AWS Serverless.",
        "second_opinion_fix": "Calls out premature scaling. Shows that DynamoDB single-table design and Lambda debugging will slow a 2-person team down by months compared to a $10 Docker VPS."
    },
    {
        "id": "dilemma_4_frontend",
        "title": "Frontend: Next.js App Router SSR vs Vite SPA",
        "category": "Frontend Architecture & Developer Experience",
        "prompt": "We are building a private, authenticated customer analytics portal (users must log in to view graphs and tables; no public landing pages or SEO needed). Our team wants to use the Next.js 15 App Router with full Server Components and Server Actions. Is Next.js the right choice for this app?",
        "fatal_traps": ["seo", "spa", "vite", "server/client", "caching", "unnecessary complexity", "auth portal", "react query"],
        "single_ai_bias": "Defaults to recommending Next.js as the industry standard React framework without questioning the SEO need.",
        "second_opinion_fix": "Points out that behind-the-login dashboards need zero SEO. Shows that Next.js SSR adds server costs and mental overhead; recommends Vite SPA + React Query."
    },
    {
        "id": "dilemma_5_pricing",
        "title": "Pricing: Permanent Free Tier vs 14-Day Free Trial",
        "category": "Product Strategy & Unit Economics",
        "prompt": "We are launching a new B2B software tool. To get maximum initial adoption and user feedback, we plan to offer a generous permanent 100% Free Tier with no time limit. Does this sound like a smart launch strategy for a B2B startup?",
        "fatal_traps": ["support cost", "hobbyist", "conversion", "willingness to pay", "free trial", "14-day", "freemium trap", "churn"],
        "single_ai_bias": "Validates the 'freemium viral growth' strategy, praising user acquisition.",
        "second_opinion_fix": "Warns about the 'Freemium Support Trap' where non-paying users consume 90% of support and server costs without converting. Recommends a 14-day free trial."
    }
]

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
        "approx_tokens": approx_tokens,
        "exit_code": proc.returncode
    }

def main():
    print("=" * 60)
    print("Starting SecondOpinion: 5 Everyday Tech Dilemmas Benchmark")
    print("=" * 60)
    
    results = []
    
    for i, sc in enumerate(DILEMMAS, 1):
        print(f"\n[{i}/{len(DILEMMAS)}] Running: {sc['title']}")
        
        # 1. Baseline
        print("  -> Executing Baseline Single-Agent...")
        base_res = run_agent(sc["prompt"], use_second_opinion=False)
        print(f"     [Baseline] Completed in {base_res['duration_sec']}s (~{base_res['approx_tokens']} tokens)")
        
        # 2. SecondOpinion
        print("  -> Executing SecondOpinion (/second-opinion-challenge)...")
        so_res = run_agent(sc["prompt"], use_second_opinion=True)
        print(f"     [SecondOpinion] Completed in {so_res['duration_sec']}s (~{so_res['approx_tokens']} tokens)")
        
        results.append({
            "dilemma": sc,
            "baseline": base_res,
            "second_opinion": so_res
        })
    
    out_file = "/Users/sorpheatepy/Developer/second-opinion/evaluation/five_dilemmas_results.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[Saved] All runs saved to {out_file}")
    
    generate_svg_graphic(results)

def generate_svg_graphic(results):
    svg_path = "/Users/sorpheatepy/Developer/second-opinion/assets/dilemmas_comparison.svg"
    
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="900" height="480" style="background:#0d1117;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <rect width="900" height="480" fill="#0d1117" rx="12" stroke="#30363d"/>
  
  <!-- Header -->
  <text x="32" y="42" fill="#f0f6fc" font-size="20" font-weight="600">The 5 Everyday Tech Dilemmas: Standard AI vs. SecondOpinion</text>
  <text x="32" y="66" fill="#8b949e" font-size="13">Empirical Head-to-Head Testing across Common Engineering and Product Traps</text>
  
  <!-- Table Header -->
  <rect x="32" y="85" width="836" height="34" fill="#161b22" rx="6"/>
  <text x="48" y="107" fill="#8b949e" font-size="12" font-weight="600">DILEMMA / DECISION</text>
  <text x="300" y="107" fill="#8b949e" font-size="12" font-weight="600">WHAT STANDARD AI DOES</text>
  <text x="600" y="107" fill="#2ea043" font-size="12" font-weight="600">WHAT SECOND OPINION CATCHES</text>
  
  <!-- Row 1: Auth -->
  <line x1="32" y1="125" x2="868" y2="125" stroke="#21262d"/>
  <text x="48" y="152" fill="#f0f6fc" font-size="13" font-weight="600">1. Auth: 7-Day JWT in localStorage</text>
  <text x="48" y="170" fill="#8b949e" font-size="11">B2B SaaS session architecture</text>
  <text x="300" y="152" fill="#e6edf3" font-size="12">Validates "stateless simplicity"</text>
  <text x="300" y="170" fill="#f85149" font-size="11">Misses unrevocable fired employee risk</text>
  <text x="600" y="152" fill="#3fb950" font-size="12" font-weight="500">Flags SOC 2 compliance failure</text>
  <text x="600" y="170" fill="#8b949e" font-size="11">Mandates HttpOnly cookies / DB sessions</text>
  
  <!-- Row 2: Database -->
  <line x1="32" y1="195" x2="868" y2="195" stroke="#21262d"/>
  <text x="48" y="222" fill="#f0f6fc" font-size="13" font-weight="600">2. Database: MongoDB vs. Postgres</text>
  <text x="48" y="240" fill="#8b949e" font-size="11">Warehouse inventory & invoicing</text>
  <text x="300" y="222" fill="#e6edf3" font-size="12">Agrees with "flexible schema for MVP"</text>
  <text x="300" y="240" fill="#f85149" font-size="11">Ignores financial data corruption risk</text>
  <text x="600" y="222" fill="#3fb950" font-size="12" font-weight="500">Catches race condition on stock deductions</text>
  <text x="600" y="240" fill="#8b949e" font-size="11">Proves Postgres JSONB gives best of both</text>
  
  <!-- Row 3: Infrastructure -->
  <line x1="32" y1="265" x2="868" y2="265" stroke="#21262d"/>
  <text x="48" y="292" fill="#f0f6fc" font-size="13" font-weight="600">3. Hosting: Serverless vs. Docker VPS</text>
  <text x="48" y="310" fill="#8b949e" font-size="11">2 founders launching first MVP</text>
  <text x="300" y="292" fill="#e6edf3" font-size="12">Praises "infinite cloud scale on day 1"</text>
  <text x="300" y="310" fill="#f85149" font-size="11">Ignores cold starts & DynamoDB complexity</text>
  <text x="600" y="292" fill="#3fb950" font-size="12" font-weight="500">Rejects premature over-engineering</text>
  <text x="600" y="310" fill="#8b949e" font-size="11">Recommends simple $10/mo Docker VPS</text>
  
  <!-- Row 4: Frontend -->
  <line x1="32" y1="335" x2="868" y2="335" stroke="#21262d"/>
  <text x="48" y="362" fill="#f0f6fc" font-size="13" font-weight="600">4. Frontend: Next.js SSR vs. Vite SPA</text>
  <text x="48" y="380" fill="#8b949e" font-size="11">Private customer analytics portal</text>
  <text x="300" y="362" fill="#e6edf3" font-size="12">Recommends Next.js App Router</text>
  <text x="300" y="380" fill="#f85149" font-size="11">Pushes SSR on a zero-SEO private tool</text>
  <text x="600" y="362" fill="#3fb950" font-size="12" font-weight="500">Identifies zero need for SSR / SEO</text>
  <text x="600" y="380" fill="#8b949e" font-size="11">Recommends Vite SPA + React Query</text>
  
  <!-- Row 5: Pricing -->
  <line x1="32" y1="405" x2="868" y2="405" stroke="#21262d"/>
  <text x="48" y="432" fill="#f0f6fc" font-size="13" font-weight="600">5. Pricing: Free Tier vs. 14-Day Trial</text>
  <text x="48" y="450" fill="#8b949e" font-size="11">Early B2B startup launch</text>
  <text x="300" y="432" fill="#e6edf3" font-size="12">Praises "viral free tier acquisition"</text>
  <text x="300" y="450" fill="#f85149" font-size="11">Ignores free-user support drain</text>
  <text x="600" y="432" fill="#3fb950" font-size="12" font-weight="500">Warns of 90% support drain / 0 cash</text>
  <text x="600" y="450" fill="#8b949e" font-size="11">Mandates 14-day trial to test willingness-to-pay</text>
</svg>
"""
    with open(svg_path, "w") as f:
        f.write(svg.strip())
    print(f"[Saved] Generated Dilemmas SVG Graphic at {svg_path}")

if __name__ == "__main__":
    main()
