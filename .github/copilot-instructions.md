<!-- Copilot / AI agent instructions for Fun-coding-challenges -->
# Copilot instructions — Fun-coding-challenges

This repository is a flat collection of standalone Python scripts (interactive CLI programs and small demos). The goal for an AI coding agent is to quickly find, run, and modify individual scripts while respecting the repository's filename and input conventions.

- Project shape: a single top-level folder of many single-file Python scripts (no package layout, no tests, no CI files). Examples: `Acsii Art.py`, `Pokémon API.py`, `Mastermind.py`.
- Execution: run scripts directly with the system Python 3 interpreter. Many filenames contain spaces or non-ASCII characters — always quote paths when running from a shell. Example:

  - Run ASCII art: `python3 "Acsii Art.py"`
  - Run Pokédex: `python3 "Pokémon API.py"`

- Dependencies: individual scripts install their own runtime requirements. Inspect the top of a script for imports. Common dependencies in this repo: `Pillow` (PIL) and `colorama`. Example install:

  - `python3 -m pip install pillow colorama`

- Data files & integration points:
  - `Pokémon_character_stats.json` is used by `Pokémon API.py` as a local data source. Keep JSON filenames and paths exact (case- and diacritic-sensitive).

- Patterns and conventions discovered in the codebase (do not invent these):
  - Scripts are interactive CLIs that read from `input()` and print to stdout; many clear the terminal using `print("\033c", end="")` — tests or automated runs should account for that.
  - Filenames contain spaces, punctuation, and Unicode; when editing or running, always use quoted paths or safe filename transformations.
  - Expect scripts to raise `FileNotFoundError` when passed wrong paths (e.g., `Acsii Art.py` expects an image path). Prefer validating existence before edits.
  - Visual/terminal output often uses `colorama` to colorize text; modifications to color use the `Fore`, `Back`, and `Style` APIs.

- Quick code-reading tips:
  - Entry point is usually the bottom of each `.py` file (no `if __name__ == "__main__"` convention enforced). Search the file for a `try:` loop or main program block.
  - Look for local data files referenced by exact filename strings (e.g., `Pokémon_character_stats.json`) rather than dynamic imports.

- Editing guidelines for AI edits:
  - Keep changes minimal and localized to a single script unless the user asks for a cross-cutting refactor.
  - Preserve original filename and quoting conventions; if renaming files, update all references (shell examples, in-file opens).
  - When adding dependencies, include a short note in the PR description recommending `python3 -m pip install ...` (this repo has no requirements file by default).

- Debug / run examples (shell):

  - Install deps:

    python3 -m pip install pillow colorama

  - Run a script with spaces/unicode in its name:

    python3 "Acsii Art.py"
    python3 "Pokémon API.py"

- What not to assume:
  - There is no package entrypoint or tests; do not try to run a test runner by default.
  - Do not assume modern packaging, virtualenvs, or a specific Python minor version beyond Python 3.

If anything in this summary is unclear or you'd like the instructions expanded (examples for editing, a recommended requirements.txt, or adding a README), tell me which part to expand and I'll update the file.
