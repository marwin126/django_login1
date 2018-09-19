from django.shortcuts import render,redirect
from login.models import User
# Create your views here.
def register(request):

    return  render(request,'login/register.html')

def registerDB(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=User()
    user.username=username
    user.password=password
    user.save()
    return render(request,'login/register_success.html',{'username':username})

def login(request):

    return render(request, 'login/login.html', )

def login_check(request):
    username1=request.POST.get('username')
    password1=request.POST.get('password')

    #print(username1+':'+password1)

    user=User.objects.get(username=username1)
    password2=user.password
    if password1 == password2:

        return  render(request,'login/login_success.html',{'username':username1})
    else:
        return redirect('/login',)