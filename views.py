from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings


def route_to_home(request):
    return redirect(reverse("about-me-home"))
