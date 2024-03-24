#!/bin/bash

echo "Installing libraries"

pip install Flask
pip install flask-cors

npm install
npm install nodejs
npm install axios

echo "Starting server.."

cd app
python3 run.py &

echo "Starting Vue.js..."
cd frontend/cb_viagens
npm install
npm run serve
