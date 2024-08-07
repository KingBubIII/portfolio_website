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
    
    return render(request, 'about_me_home.html', context)