#!/bin/bash

echo "Instalando as Bibliotecas"

pip install Flask
pip install flask-cors

npm install
npm install nodejs
npm install axios

echo "Iniciando servidor..."
#garantindo que está na pasta app
cd app
python3 run.py &

# Iniciar o Vue.js
echo "Iniciando Vue.js..."
cd frontend/cb_viagens
npm install
npm run serve
