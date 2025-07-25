from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.resume_upload, name='resume_upload'),
    path('list/', views.resume_list, name='resume_list'),
    path('', views.home, name='home'),
]
