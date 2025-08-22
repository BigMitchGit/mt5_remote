# AGENTS
Agent quick reference: build, test, lint, and style for this repository.

Purpose
- Current goal: repurpose this repository to provide remote execution on MetaTrader 5 (MT5) terminals. The main objective is cross-platform remote MT5 terminal access — allow computer A to send MT5 operations to computer B.
- Platform notes: Support includes Linux and Windows. Because MT5 runs primarily on Windows, the remote endpoint should expose MT5 via a Windows Python interpreter (either on linux through wine or native windows). The orchestrator can run on Linux or Windows; the key requirement is that the remote MT5 terminal is accessible from the remote Python process.

Build / install
- pip install -r requirements.txt
- pip install -e .    # editable install for development

Lint / format
- format: black .
- imports: isort . ; lint: flake8 .  # optional, install dev tools first

Tests
- all tests: pytest -q
- single file: pytest tests/test_01.py -q
- single test: pytest tests/test_01.py::test_name -q  # replace test_name

Style rules (high level)
- Imports: stdlib, third-party, local; use absolute imports inside package
- Naming/types/errors: snake_case funcs/vars, PascalCase classes, UPPER_SNAKE constants; add type hints for new code; catch specific exceptions and log+raise
- Testing: keep tests deterministic, fast, and avoid external network interactions
