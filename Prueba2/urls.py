"""
Definition of urls for Prueba2.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('ConexionMongoDB/', views.ConexionMongoDB, name='ConexionMongoDB'),
    path('ConexionMysql/', views.ConexionMysql, name='ConexionMysql'),
    path('ConexionMysql/', views.ConexionMysql, name='ConexionMysql'),
    path('TranspasoMongoDB_Mysql/', views.TranspasoMongoDB_Mysql, name='TranspasoMongoDB_Mysql'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
