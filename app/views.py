from django.shortcuts import render
from .models import Blog,Contact
# Create your views here.

def blog_view(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}

    return render(request,'index.html',context)

def blog_detail_view(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}

    return render(request,'detail.html',context)

def contact_views(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country = request.POST.get('country')
        subject = request.POST.get('subject')
        contact = Contact(first_name = firstname,last_name = lastname,country=country,subject=subject)
        contact.save()
        print("Siz Post request yubordingiz")
    return render(request,'contact.html')