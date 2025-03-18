from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsflow_home, name='newsflow_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='newsflow_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='newsflow_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='newsflow_delete')
]
