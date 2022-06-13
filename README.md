# mpulse-mobile
Django application to manage members 

## Local Setup
 - Clone repo locally
 - Create virtual environment and install python libraries
```
cd mpulse-mobile
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Create sensitive settings file
```
cp mpulse_mobile/env.sample.py mpulse_mobile/env.py
```
- Create database 
```
psql postgres
postgres=# CREATE DATABASE
<database_name>;

CREATE USER <username> WITH PASSWORD '<password>';

GRANT ALL PRIVILEGES ON DATABASE <database_name> TO username;
```
- Update `mpulse_mobile/env.py` file with your postrgres DB or default SQLite credentials. Don't forget to also add a `SECRET_KEY` variable.

- Run migrations
```
python manage.py migrate
```
- Create yourself as a superuser and add your `USERNAME` and `PASSWORD` to `mpulse_mobile/env.py`
```
python manage.py createsuperuser
Username: <username>
Email: <email (if you want, or skip)>
Password: **********
Password (again): *********
```
## Start app
- Start Django app
```
# from /mpulse-mobile
source venv/bin/activate
python manage.py runserver
```
- Now visit `http://127.0.0.1:8000/admin/` and login using the superuser credentials you created! 



## CSV Uploader

- To use CSV uploader, go to BASEURL/`upload-csv` in your browser