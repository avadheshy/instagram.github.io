from django.shortcuts import render
from app.models import user


# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        user_data=request['user_data']
        first_name=request['first_name']
        last_name=request['last_name']
        password= request['password']
        #person=user(user_data=user_data,first_name=first_name
        #last_name=last_name,password=password)
        #person.save()

    else:
        return render(request, 'register.html')
