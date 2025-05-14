# USER MANAGEMENT SYSTEM
## Purpose
This is a management system that add users and with a CRUD functionality.

## Stacks Used
1. Django
2. django-rest framework
3. Postman used for api testing
4. Db.sqlite3 as the database

## Setting up instructions
1. created a new folder called userapi
2. created a new project at the terminal: django-admin startproject user_api
3. created a new app at the terminal: python manage.py startapp users
4. in settings.py  I added users and rest_framework at installed apps
5. Imported User model from django.contrib.auth.models
6. created serializers.py; added the class UserSerializers; added various instances
7. in views.py I created my views to perform CRUD operations:
    - UserCreateView: to post new users
    - UserDetailView: to get new users
    - ChangePasswordView: to update passwords
    - UserListView: to get all the users registered


