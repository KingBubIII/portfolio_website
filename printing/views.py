from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from json import load
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
import environ
from .forms import EmailContact
from json import load

def printingHome(request):

    # del request.session["email_sent"]
    # del request.session["email_form"]

    try:
        request.session["email_sent"]
    except KeyError as e:
        request.session["email_sent"] = None

    try:
        request.session["email_form"]
    except KeyError as e:
        request.session["email_form"] = {
                                            "name": "",
                                            "email": "",
                                            "budget": "",
                                            "message": ""
                                        }

    printing_info = load(open(str(settings.BASE_DIR) + "\\printing\\static\\JSON\\about_printing.json"))

    context = {"email_sent": request.session["email_sent"],
                "email_form": request.session["email_form"],
                "printing_img_paths": printing_info["printing_images"],
                "intro": printing_info["intro"],
                "section_scrollers": printing_info["section_scrollers"]}

    return render(request, "printing_home.html", context)

def sendEmail(request):
    if request.method == "POST":
        print(request.FILES)
        # put form data into class to be extracted
        contact_form = EmailContact(request.POST, request.FILES)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            env = environ.Env()
            env.read_env()
            # build email obj
            email_msg = EmailMessage(subject= f"3D Print Inquiry - {contact_form.cleaned_data["name"]}",
                                                body= contact_form.cleaned_data.get("message") + contact_form.cleaned_data.get("budget"),
                                                from_email= env("FROM_EMAIL"),
                                                to= [contact_form.cleaned_data["email"]],
                                                bcc=[env("BCC_EMAIL")]
                                                )
            # get file user uploaded
            uploaded_file = contact_form.cleaned_data["user_model"]
            # attach to email
            email_msg.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            # send email to user and myself bcc
            email_msg.send()

            request.session["email_sent"]= True
            request.session["email_form"] = {}

            temp_url = reverse("3d-printing-home")
            return redirect(temp_url+"#email-form")
        else:
            print(contact_form.errors)

            print(request.POST.get("name"))

            request.session["email_sent"] = False
            request.session["email_form"] = {
                                                "name": contact_form.cleaned_data.get("name"),
                                                "email": contact_form.cleaned_data.get("email"),
                                                "budget": contact_form.cleaned_data.get("budget"),
                                                "message": contact_form.cleaned_data.get("message")
                                            }

            temp_url = reverse("3d-printing-home")
            return redirect(temp_url+"#email-form")
