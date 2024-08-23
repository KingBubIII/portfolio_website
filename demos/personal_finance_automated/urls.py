from django.urls import path

from . import views

urlpatterns = [
    # path("", views.home, name="personal_finance_home"),
    path("", views.personal_finance_automated),
    path("recalculate/", views.recalculate),
]
