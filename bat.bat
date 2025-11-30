@echo off
echo === Django Superuser Creator ===

set /p USERNAME=Enter username: 
set /p EMAIL=Enter email: 
set /p PASSWORD=Enter password: 

(
  echo from django.contrib.auth import get_user_model;
  echo User = get_user_model();
  echo User.objects.create_superuser("%USERNAME%", "%EMAIL%", "%PASSWORD%");
) | python manage.py shell

echo Superuser created!
pause
