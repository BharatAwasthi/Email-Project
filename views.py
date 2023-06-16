from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core.mail import send_mail, EmailMessage
# from .utils import send
# Create your views here.
# # email_app/views.py
from django.conf import settings
from .models import mode 
# from django.core.mail import send_mail

# def send_email(request):
#     subject = 'Hello from Django!'
#     message = 'This is a test email sent from Django.'
#     from_email = settings.EMAIL_HOST_USER  # Replace with your email address
#     recipient_list = ['dmellowsiddharth@gmail.com', ]  # List of recipient email addresses
    
#     send_mail(subject, message, from_email, recipient_list)
    
#     return HttpResponse('Email sent successfully.')
# def  index_page(request):
#     return render (request, 'index.html')

# def mail_s(request):
#     if request.method=='POST':
#         send()
#     return redirect('/')

def send_mail(request):
        
    if request.method =='POST':
        data=mode
        data.name=request.POST.get('name')
        data.s_email=request.POST.get('email')
        data.designation=request.POST.get('message')
        data.phone=request.POST.get('phone')
        email=EmailMessage(
            'Your Response',
            f'Hi there {data.name}!\n , Thanks for your response we will update you soon. By the time have a look at your response: \n \n Your name: {data.name}\n Your email: {data.s_email}\n Your phone number: {data.phone} \n You applied for the position of: {data.designation}',
            settings.EMAIL_HOST_USER,
            [data.s_email]
        )
        email.fail_silently= True
        email.send()
    
    return render (request, 'index.html')