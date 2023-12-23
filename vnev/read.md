# Django Outh2 provider

### This is the process how, I build this authentication system.
#
#
#### Step 1 : Create Django Project (In main python djngo must installed or use virtual environemnt)
```
django-admin startproject dj_auth
```

#### Step 2 : Install requirement in virtual environemnt
```
pip install -r requirements.txt
```

#### Step 3 : Create user app 

```
python manage.py startapp users
```

#### Step 4 : Add extra model and extra feild for user if you have. Add register & login views and urls. Add users api in django_auth.urls
#
#
# Main step to create authentication system
#
#### Step 5 : Create database tables.
```
python manage.py makemigrations
python manage.py migrate
```

#### Step 6 : Create super user. (Enter username and password.)
```
python manage.py createsuperuser
```

#### Step 7 : Now create authentication aplication with following details. That will genrate client_id and client Secret. (Confidencial)

```
python manage.py runserver
```

-  Hit URL: http://127.0.0.1:8000/o/applications/register/ (Enter super user's username and password)
-  Enter the name of application. Before save take note of Client id and Client secret, we will use it in a minute. After save client secret will be hashed.
-  Set Values : Client type = confidential, Authorization grant type = Resource owner passowrd-based, Add redirect urls also.
- Save it. And create .env file add client and client-secret there.

### NOTE: I made some changes in login and register process according to mine. Which is diffrent from official document of outh2_provider
### Oficial link : https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html
#
#
#### Step 8 : Register user : 
METHOD : POST
URL : http://127.0.0.1:8000/users/register/
Content-type: application/x-www-form-urlencoded
BODY: username, password, confirm_password, is_active

### Login
METHOD: POST
URL: http://127.0.0.1:8000/users/login/
Content-type: application/x-www-form-urlencoded
BODY: email and password (In my case)
