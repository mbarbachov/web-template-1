from django.shortcuts import render, redirect
from nylas import APIClient
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# set up nylas client
print(config.get('CLIENT_ID'))
nylas = APIClient(config.get('CLIENT_ID'), config.get('CLIENT_SECRET'), config.get('ACCESS_TOKEN'))


def home(request):
    return render(request, 'base/mainPage.html')


def about(request):
    return render(request, 'base/template.html')


def service(request):
    return render(request, 'base/template.html')


def contacts(request):
    return render(request, 'base/template.html')


def send_email(request):
    # send the email from a get request
    draft = nylas.drafts.create()

    # configure the draft
    draft.subject = "FORM REQUEST"
    draft.body = "This email content should be the description of the user order including their email anf info \n" \
                 " along with order information"
    draft.to = [{'name': 'Michael', 'email': 'creeperarcade2.0@gmail.com'}]

    try:
        # attempt to send an email
        draft.send()
        print("Success")
    except:
        # email failed to send for some reason
        print('Fail')

    return redirect('base-home')
