from email import message
from django.shortcuts import redirect, render
from app.models import person
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        print('inside the post method')
        user_data = request.POST['username']
        password = request.POST['password']
        if person.objects.filter(user_data=user_data).exists():
            people = person.objects.exclude(user_data=user_data)

            context = {
                'name': user_data,
                'all': people,
            }
            for x in context['all']:
                print(x.user_data)
            return render(request, 'login.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')


def register(request):
    if request.method == 'POST':
        mail = request.POST['mail']
        first_name = request.POST['first_name']
        last_name = request.POST.get('last_name', False)
        password = request.POST['password']
        if person.objects.filter(mail=mail).exists():
            messages.info(request, 'user allready exist')
            return redirect('register')
        else:
            obj = person(mail=mail, first_name=first_name,
            last_name=last_name, password=password, phone=None,
            location=None, bio=None, picture=None, gender=None)
            obj.save()
            return redirect('/')


    else:
        return render(request, 'register.html')
