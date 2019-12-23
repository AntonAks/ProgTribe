# ProgTribe Project

## About 
This is the web application build with Django and Wagtail.
Basic functionality:
* Blog (Wagtail CMS)
* Quiz related with IT knowledg (in dev) 

## How to install and run
1. clone dev branch 
2. install virtual env `virtualenv -p python3.7 <name>`
3. install requarements: pip3 install -r requirements.txt
4. create local_settings.py (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASES)
5. python3 manage.py makemigrations blog
6. python3 manage.py migrate
7. python3 manage.py createsuperuser
8. `127.0.0.1:8000/cms/` - opens wagtail CMS engine
