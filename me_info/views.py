from django.shortcuts import render
from django.conf import settings
from json import load

# Create your views here.
def intro(request):
    intro_data = load(open(settings.JSON_PATH + "about_me.json"))["intro"]
    intro_data["image_paths"] = [settings.MEDIA_URL + img for img in intro_data["image_paths"]]

    projects_data = load(open(settings.JSON_PATH + "about_me.json"))["projects"]

    context = {"intro_data": intro_data, "projects_data": projects_data}

    return render(request, "intro.html", context)

def work_history(request):
    work_history_data = load(open(settings.JSON_PATH + "about_me.json"))["work_history"]
    for job_index in range(len(work_history_data)):
        work_history_data[job_index]["company_image"] = settings.MEDIA_URL + work_history_data[job_index]["company_image"]

    projects_data = load(open(settings.JSON_PATH + "about_me.json"))["projects"]

    context = {"work_history_data": work_history_data, "projects_data": projects_data}
    return render(request, "work_history.html", context)

def projects(request):
    projects_data = load(open(settings.JSON_PATH + "about_me.json"))["projects"]
    context = {"projects_data": projects_data}
    return render(request, "projects.html", context)