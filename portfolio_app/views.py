from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/project_list.html', {'projects': projects})
# Create your views here.
from django.shortcuts import render

def landing_page(request):
    context = {
        'name': 'Basit Shameem',
        'title': 'Software Developer',
        'bio': ("Hi! I’m Basit Shameem, a passionate Software Developer specializing in Python, AI/ML, Django, "
                "Flask, and full-stack web development. Based in Mohali, Punjab, I enjoy turning complex problems "
                "into simple, beautiful, and intuitive solutions."),
        'email': 'baeri1010@gmail.com',
        'location': 'Mohali, Punjab',
        'linkedin': 'https://www.linkedin.com/in/basit-shameem-0a8907188/',
        'github': 'https://github.com/baBa0102',
        'skills': ['Python', 'AI/ML', 'Django', 'Flask', 'Front End', 'Back End']
    }
    return render(request, 'portfolio_app/landing_page.html', context)
from .models import Experience, Education

def experience_list(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'portfolio_app/experience_list.html', {'experiences': experiences})

def education_list(request):
    educations = Education.objects.all().order_by('-start_year')
    return render(request, 'portfolio_app/education_list.html', {'educations': educations})
