#!/usr/bin/env bash
set -e

# SecondOpinion Universal Installer
# Automatically detects installed AI coding runtimes and registers skills via symlinks.

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO_DIR/skills"

echo "Installing SecondOpinion skills from: $SKILLS_DIR"

TARGET_DIRS=(
  "$HOME/.claude/skills"
  "$HOME/.gemini/config/skills"
  "$HOME/.gemini/antigravity-cli/skills"
  "$HOME/.agents/skills"
)

INSTALLED_COUNT=0

for target in "${TARGET_DIRS[@]}"; do
  mkdir -p "$target"
  for skill in "$SKILLS_DIR"/second-opinion*; do
    if [ -d "$skill" ]; then
      skill_name=$(basename "$skill")
      ln -sfn "$skill" "$target/$skill_name"
      INSTALLED_COUNT=$((INSTALLED_COUNT + 1))
    fi
  done
  echo "Registered skills into: $target"
done

echo "Successfully registered SecondOpinion across all detected AI agent runtimes."
