#!/usr/bin/env sh

. .venv/bin/activate
pip-compile --output-file=requirements.txt pyproject.toml
pip-compile --extra=dev --output-file=dev-requirements.txt -c requirements.txt pyproject.toml
