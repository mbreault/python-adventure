# Repository Guidelines

## Project Structure & Module Organization
- Source lives in `adventure/` (core modules: `game.py`, `data.py`, `model.py`, `prompt.py`, `__main__.py`, `__init__.py`).
- Game data: `adventure/advent.dat`.
- Tests live in `adventure/tests/` (unittest + doctest text files).
- CLI entry: `python -m adventure`; simple runner: `play.py`.

## Build, Test, and Development Commands
- Run game locally: `python -m adventure` (interactive prompt) or `python play.py`.
- Run tests: `python -m unittest -v` (discovers `test_*.py` and doctests via `load_tests`).
- Build sdist: `python setup.py sdist` (creates a source distribution).

## Coding Style & Naming Conventions
- Python 3, 4‑space indentation, PEP 8 naming: modules `snake_case`, classes `CapWords`, functions `lower_snake_case`.
- Keep output text uppercase to match the original game style.
- Avoid introducing new runtime dependencies; prefer standard library.
- Place new package code under `adventure/`; keep tests under `adventure/tests/`.

## Testing Guidelines
- Framework: `unittest` with doctests. Add new tests as `adventure/tests/test_*.py`.
- Add scenario docs as doctest `.txt` files and wire them via the existing `load_tests` in `test_walks.py`.
- Run all tests with `python -m unittest`; ensure changes don’t break walkthroughs.
- For game logic, add reproducible cases using `Game(seed=...)` or `create_game(seed=...)`.

## Commit & Pull Request Guidelines
- Commits: imperative mood and focused (e.g., "Add API for programmatic play"). Group related changes; avoid drive‑by refactors.
- PRs: include a clear description, linked issues, testing notes (`unittest` output), and before/after examples when user‑visible text changes.
- Do not change file layout or data format without explaining migration impact.

## Agent Notes
- Keep changes minimal and scoped; do not modify unrelated files.
- Update this guide or `README.md` when adding commands or public APIs (`create_game`, `send_command`).
