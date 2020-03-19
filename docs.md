## First Time

cd backend/

docker run -d \
  --name djangodev \
  -v ${PWD}:/app \
  -v ${PWD}/db:/var/lib/postgresql/11/main \
  -v ${PWD}/venv:/app/venv \
  -p 8000:8000 \
  python:3.8.2-slim \
  tail -f /dev/null

docker exec -it ID bash

chmod +x /app/init.sh
/app/init.sh

cd /app
pip install virtualenv
virtualenv /app/venv
source /app/venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
echo "from accounts.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

## Running an Existing Container

docker ps -a
docker restart ID
docker exec -it ID bash
service postgresql restart
source /app/venv/bin/activate

## Running Django App

python manage.py runserver 0.0.0.0:8000


## Testing

python manage.py test