virtualenv -p C:/Users/nhatminh.phuong/AppData/Local/Continuum/Anaconda3/python.exe env
source env/Scripts/activate
pip install -r requirements.txt
django-admin startproject mysite 
django-admin startapp blog
python manage.py migrate
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py createsuperuser

(pythonanywhere)
pip3.6 install --user pythonanywhere
pa_autoconfigure_django.py https://github.com/minhchan11/Django_Practice.git
python manage.py createsuperuser 
python manage.py collectstatic
(/pythonanywhere)