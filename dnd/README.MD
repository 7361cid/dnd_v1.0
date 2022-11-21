Пошаговый лог создания django приложения  
0) pip install django    и  pip install pillow 
1) django-admin startproject dnd
2) python manage.py startapp client, внести приложение в настройки  
AUTH_USER_MODEL = 'name_of_app.NameOfModel'
3) python manage.py makemigrations  python manage.py migrate
4) форма регистрации 
5) представления для регистрации, входа и выхода
6) добавление ссылок
7) Создание шаблона + статика css
