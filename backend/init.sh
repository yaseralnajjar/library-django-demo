apt update
apt -y upgrade

apt-get -y install python3-dev libpq-dev postgresql postgresql-contrib
service postgresql restart

su - postgres -c "psql -c \"CREATE DATABASE dbapp;\""

create_user_queries=$"
  CREATE USER dbuser WITH PASSWORD 'dbpass';
  ALTER ROLE dbuser SET client_encoding TO 'utf8';
  ALTER ROLE dbuser SET default_transaction_isolation TO 'read committed';
  ALTER ROLE dbuser SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE dbapp TO dbuser;
"

su - postgres -c "psql -c \"${create_user_queries}\""
