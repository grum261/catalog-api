$!/bin/bash
source /home/grum231/.local/share/virtualenvs/catalog-app-OHzCji5G/bin/activate
exec gunicorn --config "/home/grum231/prog/python/catalog/catalog_app/gunicorn_config.py" catalog.wsgi