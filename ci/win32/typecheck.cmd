REM script to run mypy type checker on this source tree.
pushd .
cd /D "%~dp0"
cd ..\..\
call .\venv\Scripts\activate
set PYTHONPATH=.\src\kpicalculator;%$PYTHONPATH%
python -m mypy ./src/kpicalculator ./unit_test/
popd