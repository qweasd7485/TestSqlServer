from django.conf.urls import url
from L2Daily import views

app_name = 'L2Daily'
urlpatterns = [
    #url(r'^about/', views.about, name='about'),
    
    url('.*', views.L2Daily, name='L2Daily'),
]
