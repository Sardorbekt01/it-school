from django.shortcuts import render
from django.urls import reverse

def post(request):
    return render(request,'index.html',{})
def home(request, pk):
    return render(request, 'index.html', {'pk': pk})
def about(request, pk):
    return render(request, 'about.html', {'pk': pk})
def blog(request, pk):
    return render(request, 'blog.html', {'pk': pk})
def contact(request, pk):
    return render(request, 'contact.html', {'pk': pk})
def error(request, pk):
    return render(request, '404.html', {'pk': pk})
def project(request, pk):
    return render(request, 'project.html', {'pk': pk})
def service(request, pk):
    return render(request, 'service.html', {'pk': pk})
def team(request, pk):
    return render(request, 'team.html', {'pk': pk})
def testimonial(request, pk):
    return render(request, 'testimonial.html', {'pk': pk})
