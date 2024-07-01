from django.shortcuts import render
from settings import MEDIA_URL, BASE_DIR, JSON_PATH, STATIC_URL
from os import listdir
from json import load

# Create your views here.
def intro(request):
    intro_data = load(open(JSON_PATH + "about_me.json"))["intro"]
    intro_data["image_paths"] = [MEDIA_URL+img for img in intro_data["image_paths"]]

    return render(request, "me_info\\intro.html", intro_data)

def work_history(request):
    work_history_data = load(open(JSON_PATH + "about_me.json"))["work_history"]
    context = {"work_history_data": work_history_data}
    return render(request, "me_info\\work_history.html", context)

def projects(request):
    projects_data = load(open(JSON_PATH + "about_me.json"))["projects"]
    context = {"projects_data": projects_data}
    return render(request, "me_info\\projects.html", context)