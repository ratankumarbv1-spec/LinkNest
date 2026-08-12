from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),

    path('dashboard/' , views.dashboard , name = 'dashboard'),

    path('add/', views.add_link, name='add_link'),

    path('edit/<int:link_id>/', views.edit_link, name='edit_link'),

    path('delete/<int:link_id>/', views.delete_link, name='delete_link'),


]