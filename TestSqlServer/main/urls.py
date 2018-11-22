from django.conf.urls import url
from main import views

app_name = 'main'
urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url('.*', views.main, name='main'),    
]
