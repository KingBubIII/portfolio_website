from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.conf import settings


def route_to_home(request):
    return redirect(reverse("about-me-home"))


def click(request):
    hidden_button_id = request.GET.get("id")
    print(request.session.get_session_cookie_age())
    if not hidden_button_id in request.session["hidden_buttons_found"]:
        request.session["hidden_buttons_found"].append(hidden_button_id)

    return HttpResponse(len(request.session["hidden_buttons_found"]))
