from django.shortcuts import render
from settings import MEDIA_URL, BASE_DIR, STATIC_URL
from os import listdir

# Create your views here.
def home(request):
    images_dir = listdir(str(BASE_DIR)+"\\devsite\\me_info\\static\\img\\")
    images_paths = [MEDIA_URL+img for img in images_dir]
    # inital_image_path = images_paths.pop(0)
    context = {"image_paths": images_paths}
    return render(request, "me_info\\index.html", context)