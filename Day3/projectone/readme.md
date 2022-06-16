##Start a project
pip install django<br>
django-admin startproject webapp<br>
cd webapp<br>
django-admin startapp Myapp<br>
mkdir templates<br>
code .<br>
in webapp goto setting.py<br>
In installed apps..enter add your appname "Myapp" and ,
<br>
scroll down<br>
in add DIRS['templates']
<br>
in templates folder add your html file<br>
<br>
in views <br>
add your function<br>
def subtract(request1):<br>
    return render(request1,"sub.html")
    <br>
in webapp .. urls.py  <br>
from django.conf.urls import url  <br>
from django.contrib import admin  <br>
from Myapp import views  <br>

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('addition',views.add),
    url('subtraction',views.subtract)]
    


python manage.py runserver
