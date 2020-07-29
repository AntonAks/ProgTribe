# WagSite Project
![alt text](https://github.com/AntonAks/WagSite/blob/dev/wagsite_image.png?raw=true)

## About 
This is a template application for basic website, built with Wagtail CMS. 

## How to install and run
1. clone master branch 
2. install virtual env `virtualenv -p python3.8 <name>`
3. install requirements: pip3 install -r requirements.txt
4. create local_settings.py (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASES, INTERNAL_IPS)
5. `python manage.py makemigrations blog`
6. `python manage.py migrate`
7. `python manage.py update_translation_fields`
8. `python manage.py createsuperuser`
9. `python manage.py runserver`
10. `127.0.0.1:8000/admin` - opens wagtail CMS engine

## Wagtail CMS simple guide
0. Delete existing root page
1. Create new root page using Blog Home page
2. Open `+ ADD CHILD PAGE`
3. Open `BlogPage`
...
