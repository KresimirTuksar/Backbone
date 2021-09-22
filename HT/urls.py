"""HT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from backbone import views

urlpatterns = [
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/uploads/form/', views.model_form_upload, name='upload'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name= 'logout'),
    path('', views.mjesta, name='mjesta'),
    path('backbone/mjesta/<str:pk>/', views.podrucja, name='podrucja'),
    path('backbone/mjesta/<str:pk>/novi_unos', views.podrucje_novo, name='podrucje_novo'),
    path('backbone/novi_unos/', views.mjesto_novo, name='mjesto_novo'),
    

    #path('backbone/<str:pk>/novi_unos/', views, name=''),
    #path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/', views.odk, name='odk'),
    #path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/novi_unos', views.odk_novo, name='odk_novo'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/', views.dionice, name='dionice'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/novi_unos', views.dionice_novo, name='dionice_novo'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/dionice/<str:dionica_pk>/uredi', views.dionica_uredi, name='dionica_uredi'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/odk/<str:odk_pk>/', views.kablovi_odk, name='kablovi_odk'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/dionice/<str:dionica_pk>/', views.kablovi, name='kablovi'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/dionice/<str:dionica_pk>/novi_unos', views.kablovi_novo, name='kablovi_novo'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/dionice/<str:dionica_pk>/kablovi/<str:kabel_pk>/biljeska', views.biljeska_novo, name='biljeska_novo'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/dionice/<str:dionica_pk>/kablovi/<str:kabel_pk>/uredi', views.kabel_uredi, name='kabel_uredi'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/dionice/<str:dionica_pk>/kablovi/<str:kabel_pk>/odradi', views.kabel_odradi, name='odradi'),
    path('backbone/mjesta/<str:pk>/podrucja/<str:podrucje_pk>/dionice/<str:dionica_pk>/kablovi/<str:kabel_pk>/', views.kabel, name='detalji'),
]
