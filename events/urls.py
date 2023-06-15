from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.event_create, name='event_create'),
    path('<int:pk>/update/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('<int:pk>/register/', views.event_registration, name='event_registration'),
    path('register/success/<int:registration_id>/<int:pk>/', views.registration_success, name='registration_success'),
    path('<int:pk>/view_registrations/', views.view_registrations, name='view_registrations'),
    path('<int:event_id>/registrations/download/', views.download_registrations, name='download_registrations'),
    path('registrations_closed/', views.reg_closed, name='reg_closed'),
]