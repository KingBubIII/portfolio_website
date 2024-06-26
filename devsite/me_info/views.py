from django.shortcuts import render
from settings import MEDIA_URL, BASE_DIR, STATIC_URL
from os import listdir

# Create your views here.
def intro(request):
    images_dir = listdir(str(BASE_DIR)+"\\devsite\\me_info\\static\\img\\")
    images_paths = [MEDIA_URL+img for img in images_dir]

    navbar_links = {"about_me":"intro", "projects": "projects", "work_history": "work-history"}

    context = {"image_paths": images_paths}
    return render(request, "me_info\\intro.html", context)

def work_history(request):
    return render(request, "me_info\\work_history.html")