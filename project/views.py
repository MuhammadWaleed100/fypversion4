from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from .forms import loginForm
from django.core.mail import send_mail
from .models import User
import string
import random

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))
# Create your views here.
def base(request):
    return render(request,'base.html')
def tryy(request):
    return render(request,'try.html')


def contact(request):
    return render(request,'contact.html')

def newpost(request):
   return render(request,'new-post.html')

def wantajob(request):
   return render(request,'job-post.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')


def register(request):
    form=loginForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        print("haha")
    else:
        print("error")
    return render(request,'login.html')






def userlogin(request):
    em = request.POST.get('em')
    pas = request.POST.get('pas')
    rad=request.POST.get('rad')

    # obj = get_object_or_404(User, em=em,pas=pas)
    param=''
    try:
        if(rad=='ERA'):
            try:
             instance = User.objects.get(em=em,pas=pas,rad='ERA')
             return render(request, 'new-post.html')
            except:
                param = {'error': "Enter Correct Details"}
                return render(request, 'login.html',param)
        else:
            try:
             print(rad,em,pas)

             instance = User.objects.get(em=em,pas=pas,rad='JS')
             return render(request, 'job-post.html')
            except:
                param = {'error': "Enter Correct Details"}
                return render(request, 'login.html',param)
    except:
        param={'error':"Enter Correct Details"}
        return render(request, 'login.html',param)


def profile(request):
    return render(request,'profile.html')


def forget(request):
    return render(request,'forget.html')


def sendmail(request):
    em=request.POST.get('em')
    try:

        instance=User.objects.get(em=em)
        newpas=randompassword()
        print(newpas)
        User.objects.filter(em=em).update(pas=newpas)
        send_mail(
        'Your Account Reset password ',#subject portion
        'Your Account Reset password is '+newpas,#message portion
        'skills.based.recommender@gmail.com',#email from
        [em],#email to
        fail_silently=False,)
        param={'error':'Mail successfully sent..!'}
        return render(request,'login.html',param)
    except :
        param={'error':'No Record Found...! Please Enter Correct Email..!'}
        return render(request,'forget.html',param)