from django.shortcuts import render, redirect
from .models import InquiryClass
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        inquiry = InquiryClass(full_name=request.POST.get('full_name',''),email=request.POST.get('email',''),cargo=request.POST.get('cargo',''),container=request.POST.get('container',''))
        send_mail(f'From : {inquiry.full_name}',f'Email: {inquiry.email} \n Cargo: {inquiry.cargo} \n Container:{inquiry.container}','nicu1221piticu@gmail.com',['nicu1221piticu@gmail.com'],fail_silently=False)
        inquiry.save()


    return render(request, 'index.html')