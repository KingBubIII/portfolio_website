from django.shortcuts import render
from django.conf import settings
from json import load

def home(request):
    info_dict = load(open(settings.JSON_PATH + "about_me.json"))
    context = {}
    context["intro"] = info_dict["intro"]
    context["work_history"] = info_dict["work_history"]
    context["me_images"] = info_dict["me_images"]
    context["education"] = info_dict["education"]
    context["self_learning"] = info_dict["self_learning"]
    context["projects"] = info_dict["projects"]
    context["all_skills"] = list(set([skill for project in context["projects"] for skill in project["skills"]]))
    return render(request, 'home.html', context)

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