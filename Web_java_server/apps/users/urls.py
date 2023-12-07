from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('users', views.profile, name='profile'),
    # path('users/create_user', views.create_user, name='create_user')
]