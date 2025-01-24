from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='home_content')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home_images/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.title

class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='about_content')
    name = models.CharField(max_length=50)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Skilled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skilled_content')
    name = models.CharField(max_length=50)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='skill_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Enter a value between 0 and 100")  # e.g., percentage of proficiency

    def __str__(self):
        return self.skill_name

class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    project_name = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='work_images/', blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
