from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
    path("", views.route_to_home),
    path("about-me/", include("me_info.urls")),
    path('admin/', admin.site.urls),
    path("demos/", include("demos.urls"))
]

