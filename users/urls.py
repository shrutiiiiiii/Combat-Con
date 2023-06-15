from django.urls import path
from . import views
from . import models

app_name = 'users'

urlpatterns = [
    path('profile/athlete/create/', views.create_athlete, name='create_athlete'),
    path('profile/host/create/', views.create_host, name='create_host'),
    path('profile_alert/', views.profile_alert, name='profile_alert'),
    path('register/', views.register, name='register'),
    path('profile/athlete/<int:pk>/', views.athlete_profile, name='athlete_profile'),
    path('profile/host/<int:pk>/', views.host_profile, name='host_profile'),
    path('profile/hedit/<int:pk>/', views.edit_host_profile, name='edit_host_profile'),
    path('profile/aedit/<int:pk>', views.edit_athlete_profile, name='edit_athlete_profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
]