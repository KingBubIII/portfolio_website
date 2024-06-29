from django.shortcuts import render
from settings import MEDIA_URL, BASE_DIR, JSON_PATH
from os import listdir
from json import load

# Create your views here.
def intro(request):
    images_dir = listdir(str(BASE_DIR)+"\\devsite\\me_info\\static\\img\\")
    images_paths = [MEDIA_URL+img for img in images_dir]

    navbar_links = {"about_me":"intro", "projects": "projects", "work_history": "work-history"}

    context = {"image_paths": images_paths}
    return render(request, "me_info\\intro.html", context)

def work_history(request):
    work_history_data = load(open(JSON_PATH + "about_me.json"))["work_history"]
    context = {"work_history_data": work_history_data}
    return render(request, "me_info\\work_history.html", context)

def projects(request):
    return render(request, "me_info\\projects.html")