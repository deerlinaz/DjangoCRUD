from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
#app_name = 'reports'
urlpatterns = [
    #path('', views.IndexView.as_view(), name = 'display'),
    path('delete/<str:email>/<str:cname>/<str:dc>', views.delete, name='delete'),
    path('update/<str:email>/<str:cname>/<str:dc>', views.update, name='update'),
    path('', views.create, name='create'),
]