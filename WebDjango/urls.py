"""
URL configuration for WebDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views, settings
from .apps import account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login_account', views.user_login, name='user_login'),
    path('registration', views.user_registration, name='registration'),
    path('account/', include('account.urls'), name='user_account'),
    # path('news/', views.news, name='news')
]
