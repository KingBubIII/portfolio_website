from django.shortcuts import render
from django.conf import settings
from json import load


def home(request):
    info_dict = load(open(settings.JSON_PATH + "about_me.json"))

    info_dict["all_skills"] = list(
        set([skill for project in info_dict["projects"] for skill in project["skills"]])
    )

    if request.session.has_key("hidden_buttons_found"):
        print("found")
        info_dict["buttons_found"] = len(request.session["hidden_buttons_found"])
    else:
        print("not found")
        request.session["hidden_buttons_found"] = []
        info_dict["buttons_found"] = 0

    return render(request, "about_me_home.html", info_dict)
