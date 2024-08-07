from django.urls import path, include

urlpatterns = [
    path("personal_finance_automated/", include("demos.personal_finance_automated.urls"))
]
