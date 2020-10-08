# WagSite Project
![alt text](https://github.com/AntonAks/WagSite/blob/master/wagsite_image.png?raw=true)

## About 
This is a template application for basic website, built with Wagtail CMS. 

## How to install and run
1. clone master branch
2. install virtual env `virtualenv -p python3.8 <virtualenv name>`
3. `source ../<virtualenv name>/bin/activate` or `..\<virtualenv name>\Script\activate` (for windows)
4. install requirements: `pip3 install -r requirements.txt`
5. create and fill local.py file in `..WagSite\WagSite\settings\` (SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASES, INTERNAL_IPS)
6. `python manage.py makemigrations blog home`
7. `python manage.py migrate`
8. `python manage.py update_translation_fields`
9. `python manage.py createsuperuser`
10. `python manage.py runserver`
11. `127.0.0.1:8000/admin` - opens wagtail CMS engine

## Wagtail CMS simple guide
0. Delete existing root page
1. Create new root page using Blog Home page
2. In settings need to create site and choose the root page.
3. Open `+ ADD CHILD PAGE` (`BlogPage`)
4. ...
5. Profit
