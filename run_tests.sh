#!/bin/bash

# Configurações e comandos para executar os testes
export PYTHONPATH=.:./framework:./integration_tests
export CONFIG=test

python -m integration_tests.purge_queues
pytest -c int_tests.ini --disable-pytest-warnings
ret=$?
if [ "$ret" = 1 ]; then
  python -m integration_tests.purge_queues
  pytest --last-failed --last-failed-no-failures none -c int_tests.ini --disable-pytest-warnings
else
  exit $ret
fi
