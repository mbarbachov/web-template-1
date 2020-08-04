from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="base-home"),
    path('about', views.about, name="base-about"),
    path('services', views.service, name="base-services"),
    path('pricing', views.pricing, name="base-pricing"),
    path('contact', views.contacts, name="base-contacts"),
]
