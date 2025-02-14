"""
URL configuration for disaster_relief project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from DRSCM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('error404',views.error404),
    path('about',views.about),
    path('report',views.report),
    path('index',views.index),
    path('admin_dashboard',views.admin_dashboard),
    path('relief_centers',views.relief_centers),
    path('notifications',views.notifications),
    path('logistics',views.logistics),
    path('add_disaster_details',views.add_disaster_details),
    path('login',views.login),
    path('our_services', views.our_services),
<<<<<<< HEAD
    path('terms_condition',views.terms_condition),
=======
    path('contact_us',views.contact_us),
>>>>>>> 97b5f0fbba38e6b366dd338376f0b20ef7639838
]
