from django.urls import path

from . import views

urlpatterns = [path("", views.printingHome, name="3d-printing-home"),
                path("contact/", views.sendEmail, name="email-message")]
