from django.urls import path

from . import views

urlpatterns = [
    path("intro", views.intro),
    path("work-history", views.work_history)
]
