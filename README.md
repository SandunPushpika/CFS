# CFS - Course Feedback System
This project is built for the BE of a Course Feedback System of a Univerisity.

## How to get this running
1. Create a virtual environemnt and Activate it
```
python -m venv .venv
.venv\Scripts\activate
```
2. Install all dependencies
```
pip install -r requirements.txt
```
3. Create database cfs in MysqlClient
```
mysql -u root
create database cfs;
```
4. Run database migrations
```
cd project-root-directory
python manage.py migrate
```
5. Run the project
```
python manage.py runserver
```

## Important for contributors
* Make sure to run ```python manage.py makemigration``` after you modify or create a model.
* Use the existing folder structure.
* For views, try to use method based views with django rest decorators.

## Thank You!