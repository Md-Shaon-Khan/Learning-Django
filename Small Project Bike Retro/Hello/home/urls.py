from django.urls import path
from home import views

urlpatterns = [
    path("", views.garage, name="garage"),
    path("garage", views.garage, name="garage_alias"),
    path("heritage", views.heritage, name="heritage"),
    path("workshop", views.workshop, name="workshop"),
    path("contact", views.contact, name="contact"),
]