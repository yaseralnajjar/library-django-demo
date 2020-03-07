docker run -d \
  --name djangodev \
  -v ${PWD}:/app \
  -v ${PWD}/db:/var/lib/postgresql/11/main \
  -p 8000:8000 \
  python:3.8.2-slim \
  tail -f /dev/null

docker exec -it ID bash

chmod +x /app/init.sh
/app/init.sh


cd /app
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000


docker ps -a
docker restart ID