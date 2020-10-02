from django.shortcuts import render
from django.conf import settings
from main.models import Project
from django.contrib import messages


def index(request):
    if request.method == "POST":
        import requests
        from requests.exceptions import ConnectionError
        import smtplib

        try:
            url = requests.get('https://www.google.com', timeout=3)
            status = url.status_code
        except ConnectionError:
            status = "404"

        if status == "200":
            subject = request.POST.get('msg-subject')
            message = request.POST.get('msg-body')
            sender = request.POST.get('sender-name')

            proper_msg = """
            Subject = {}

            Body = {}

            Sent by {}

            Mailing service by `Website Portfolio` made by LokotamaTheMastermind
            """.format(subject, message, sender)

            email = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)

            email.starttls()

            email.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            email.login(settings.EMAIL_HOST_USER,
                        settings.EMAIL_HOST_PASSWORD)

            email.sendmail(settings.EMAIL_HOST_USER,
                           'lokotamathemastermind.portfolio@gmail.com', proper_msg)
            email.quit()

            messages.success(
                request, 'Successful delivered mail, wait for response of the developer, thank you')

        elif status == "404":
            messages.error(
                request, 'Sorry not connected to internet can\'t send email')

    latest_projects = Project.objects.all().order_by('-posted_at')[:4]

    if not latest_projects:
        empty = True
    elif latest_projects:
        empty = False

    context = {
        'settings': settings.DEBUG,
        'posts': latest_projects,
        'empty': empty
    }
    return render(request, 'landing/index.html', context)
