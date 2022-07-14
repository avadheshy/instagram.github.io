from email import message
from django.shortcuts import redirect, render
from app.models import person
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method=='POST':
        print('inside the post method')
        user_data=request.POST['username']
        password = request.POST['password']
        print('before login page')
        if person.objects.filter(user_data=user_data).exists():
            print('login page')
            return render(request,'login.html',{'name':user_data})
        else:
            print('home page')
            return redirect('/')

def register(request):
    if request.method == 'POST':
        user_data = request.POST['user_data']
        first_name = request.POST['first_name']
        last_name = request.POST.get('last_name',False)
        password = request.POST['password']
        if person.objects.filter(user_data=user_data).exists():
            messages.info(request,'user allready exist')
            return redirect('register')
        else:
            obj = person(user_data=user_data, first_name=first_name,
                        last_name=last_name, password=password)
            obj.save()
            return redirect('/')
        

    else:
        return render(request, 'register.html')
