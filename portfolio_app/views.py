from django.shortcuts import render, HttpResponse
from portfolio_app.models import Contact

# Create your views here.
# Displays Homepage
def home(request):
    # 'context' is just a dictionary:
    # context = {'name': "Omega", 'course': "Django"}
    return render(request, 'home.html')


#Displays Projectpage
def project(request):
    # return HttpResponse("This is project page (/project) ")
    return render(request, 'project.html')


#Displays Contact page
def contact(request):
    # return HttpResponse("This is contact page (/contact) ")
    if request.method=="POST":
        name = request.POST['fname'] +" "+ request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        # print(name, phone, email, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        # print("DATA is uploaded to DB")

    return render(request, 'contact.html')


#Displays About page
def about(request):
    # return HttpResponse("This is about page (/about) ")
    return render(request, 'about.html')
