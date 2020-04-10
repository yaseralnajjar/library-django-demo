version = '0.0.1'

app1 = {
    'default': True,
    'name': 'backend',
    'type': 'docker',
    'working_dir': '${BASE_DIR}/backend',
    'cleanup_dirs': ['${WORKING_DIR}/db', '${WORKING_DIR}/venv'],

    'container_name': 'djangodev',
    'start_container_command':
    '''docker run -d \
    --name djangodev \
    -v ${PWD}:/app \
    -v ${PWD}/db:/var/lib/postgresql/11/main \
    -v ${PWD}/venv:/app/venv \
    -p 8000:8000 \
    python:3.8.2-slim \
    tail -f /dev/null''',

    'init_container_command': 'bash -c "chmod +x /app/init.sh && /app/init.sh"',
    'restart_container_command': 'bash -c "service postgresql restart && source /app/venv/bin/activate && cd /app && python manage.py runserver 0.0.0.0:8000"'
}

app2 = {
    'name': 'frontend',
    'type': 'normal',
    'working_dir': '${BASE_DIR}/frontend',
    'cleanup_dirs': ['${WORKING_DIR}/node_modules'],

    'init_command': 'npm install',
    'start_command': 'npm start',
    # 'extra': {
    #    'prod': 'npm build'
    # }
}

apps = [app1, app2]
