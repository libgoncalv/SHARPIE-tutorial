PORT=$(shuf -i 3000-8000 -n 1)

cd webserver
python3 manage.py runserver localhost:$PORT &
cd ../runner
python3 manage.py runserver --port $PORT