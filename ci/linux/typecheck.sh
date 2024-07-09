#!/usr/bin/env sh

. .venv/bin/activate
python -m mypy ./src/kpicalculator ./unit_test/
