from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from json import load
import smtplib, ssl
from email.message import EmailMessage
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
                "intro": printing_info["intro"]}

    return render(request, "printing_home.html", context)

def sendEmail(request):
    if request.method == "POST":
        # put form data into class to be extracted
        contact_form = EmailContact(request.POST)
        if contact_form.is_valid():
            # build email obj
            email_msg = EmailMessage()
            email_msg.set_content(contact_form.cleaned_data.get("message") + contact_form.cleaned_data.get("budget"))
            email_msg["Subject"] = f"3D Print Inquiry - {contact_form.cleaned_data["name"]}"
            email_msg["From"]= "calebskingdombusiness@gmail.com"
            email_msg["To"] = contact_form.cleaned_data["email"]

            context=ssl.create_default_context()
            env = environ.Env()
            env.read_env()

            # create SMTP instance
            with smtplib.SMTP("smtp.gmail.com", port=587) as s:
                s.starttls(context=context)
                # login using email and "app password"
                s.login(email_msg["From"], env("EMAIL_APP_PASS"))
                # send email with a bcc to my personal email
                s.sendmail(from_addr=email_msg["From"],
                            to_addrs=[email_msg["To"], env("BCC_EMAIL")],
                            msg=email_msg.as_string())
            # return home with a message about it being sent successfully
            request.session["email_sent"]= True
            return redirect("3d-printing-home")
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
