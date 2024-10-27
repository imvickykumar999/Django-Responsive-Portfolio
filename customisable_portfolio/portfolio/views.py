from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
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

def edit_portfolio(request):
    # Get the current user's data
    home_content = Home.objects.filter(user=request.user).first()
    about_content = About.objects.filter(user=request.user).first()
    skilled = Skilled.objects.filter(user=request.user).first()

    if request.method == 'POST':
        # Update Home model
        if home_content:
            home_content.title = request.POST.get('home_title')
            home_content.subtitle = request.POST.get('home_subtitle')
            home_content.github_url = request.POST.get('home_github_url')
            home_content.linkedin_url = request.POST.get('home_linkedin_url')
            home_content.email_address = request.POST.get('home_email')
            if request.FILES.get('home_image'):
                home_content.image = request.FILES['home_image']
            home_content.save()

        # Update About model
        if about_content:
            about_content.name = request.POST.get('about_name')
            about_content.bio = request.POST.get('about_bio')
            if request.FILES.get('about_profile_image'):
                about_content.profile_image = request.FILES['about_profile_image']
            about_content.save()

        # Update Skilled model
        if skilled:
            skilled.name = request.POST.get('skilled_name')
            skilled.bio = request.POST.get('skilled_bio')
            if request.FILES.get('skilled_profile_image'):
                skilled.profile_image = request.FILES['skilled_profile_image']
            skilled.save()

        messages.success(request, 'Portfolio updated successfully!')
        return redirect('index')

    return render(request, 'portfolio/edit.html', {
        'home_content': home_content,
        'about_content': about_content,
        'skilled': skilled,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Error in registration. Please try again.')
    else:
        form = UserCreationForm()

    return render(request, 'portfolio/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('index')  # redirect to the main page or dashboard
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')
