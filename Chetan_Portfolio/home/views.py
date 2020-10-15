from django.shortcuts import render , HttpResponse
from home.models import Contacts
# Create your views here.
def home(request):
    context = {'name': 'chetan','course':'django'}
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')


def projects(request):
    return render(request,'projects.html')


def contacts(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # print(name,email,phone,desc)
        ins = Contacts(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("data has been printed on db")
    return render(request,'contacts.html')            
