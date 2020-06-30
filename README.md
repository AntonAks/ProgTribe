# WagSite Project
![alt text](https://github.com/AntonAks/WagSite/blob/dev/wagsite_image.png?raw=true)

## About 
This is a template application for basic website, built with Django and Wagtail. 


## How to install and run
1. clone dev branch 
2. install virtual env `virtualenv -p python3.8 <name>`
3. install requirements: pip3 install -r requirements.txt
4. create local_settings.py (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASES, INTERNAL_IPS)
5. `python3 manage.py makemigrations blog`
6. `python3 manage.py migrate`
7. `python3 manage.py createsuperuser`
8. `python manage.py update_translation_fields`
9. `python3 manage.py runserver`
10. `127.0.0.1:8000/admin` - opens wagtail CMS engine

## Wagtail CMS simple guide
1. Open `Page`
2. Open `+ ADD CHILD PAGE`
3. Open `BlogPage`
4. Add Title
5. Fill content block 
6. Save draft
7. Preview
8. Publish
...
