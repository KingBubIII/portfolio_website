from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="about-me-home"),
    path("intro/", views.intro),
    path("work-history/", views.work_history),
    path("projects/", views.projects)
]
