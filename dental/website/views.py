from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method=="POST":
        message_name=request.POST['message_name']
        message_email=request.POST['message_email']
        message=request.POST['message']
        # context

        #send mail
        send_mail(
            message_name,#subject
            message,#message
            message_email,#from email
            ['mamunurrashid1045@gmail.com'],#to email
            fail_silently=False,

            )
        return render(request,'contact.html',{'message_name':message_name})

    else:
        return render(request,'contact.html',{})
