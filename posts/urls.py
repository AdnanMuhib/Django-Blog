from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'details/<int:id>', views.details, name='details'),
]