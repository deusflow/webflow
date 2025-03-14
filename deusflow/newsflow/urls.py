from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsflow_home, name='newsflow_home'),
    path('create'. views.create, name='create')
]
