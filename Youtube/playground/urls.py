from django.urls import path
from . import views

urlpatterns = [
    path('playground/hello', views.sey_hello())
]