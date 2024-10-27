from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def index(request):
    user = request.user

    home_content = Home.objects.filter(user=user).first()
    about_content = About.objects.filter(user=user).first()
    skills = Skill.objects.filter(user=user)
    skilled = Skilled.objects.filter(user=user).first()
    works = Work.objects.filter(user=user)

    if request.method == 'POST':
        name = request.POST.get('flname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message, user=user)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')

    return render(request, 'portfolio/index.html', {
        'home_content': home_content,
        'about_content': about_content,
        'skills': skills,
        'skilled': skilled,
        'works': works,
    })
