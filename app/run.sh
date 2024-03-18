#!/bin/bash

echo "Implemente aqui o script para executar a sua solução"
python3 -m venv venv
. venv/bin/activate
pip3 install pylint
pip3 install pre-commit
pre-commit install 
pip3 install Flask