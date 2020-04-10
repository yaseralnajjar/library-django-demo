# Install required packages

apt update
apt -y upgrade

apt-get -y install python3-dev libpq-dev postgresql postgresql-contrib
service postgresql restart


# Create db table, user, password, and permissions

su - postgres -c "psql -c \"CREATE DATABASE dbapp;\""

create_user_queries=$"
  CREATE USER dbuser WITH PASSWORD 'dbpass';
  ALTER USER dbuser CREATEDB;
  ALTER ROLE dbuser SET client_encoding TO 'utf8';
  ALTER ROLE dbuser SET default_transaction_isolation TO 'read committed';
  ALTER ROLE dbuser SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE dbapp TO dbuser;
"

su - postgres -c "psql -c \"${create_user_queries}\""


# Migrate and seed admin

cd /app
pip install virtualenv
virtualenv /app/venv
source /app/venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
echo "from accounts.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell


# Start dev server

python manage.py runserver 0.0.0.0:8000