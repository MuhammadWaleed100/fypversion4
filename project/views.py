
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from .forms import loginForm
from django.core.mail import send_mail
from .models import User
import string
import random
from django.utils.crypto import get_random_string



class var:
    global uname,pas,em,rad,randnum
    def __init__(self, uname='',pas='',em='',rad='',randnum=''):
        self.uname =uname
        self.pas=pas
        self.em=em
        self.rad=rad
        self.randnum=randnum

    def getuname(self):
     return self.uname
    def getpas(self):
        return self.pas
    def getem(self):
        return self.em
    def getrad(self):
        return self.rad
    def getrandnum(self):
        return self.randnum

    def setuname(self,a):
      self.uname=a
    def setpas(self,a):
        self.pas=a
    def setem(self,a):
       self.em=a
    def setrad(self,a):
        self.rad=a
    def setrandnum(self,a):
        self.randnum=a
object=var()



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

def confirmm(request):
   object.setrandnum(get_random_string(length=6, allowed_chars='1234567890'))
   uname=request.POST.get('uname')
   object.setuname(uname)
   em=request.POST.get('em')
   object.setem(em)
   rad=request.POST.get('rad')
   object.setrad(rad)
   pas=request.POST.get('pas')
   object.setpas(pas)
   send_mail(
       'Your Account Confirmation Code ',  # subject portion
       'Your Account Confirmation Code is ' + object.randnum,  # message portion
       'skills.based.recommender@gmail.com',  # email from
       [em],  # email to
       fail_silently=False, )
   return render(request,'confirmation.html')


def register(request):
    confirmcode=request.POST.get('con')
    if(object.randnum==confirmcode):
     user = User(uname=object.uname,em=object.em,pas=object.pas,rad=object.rad)
     user.save()
     return render(request, 'login.html')
    else:
     param = {'error': "Enter Correct Code"}
     return render(request,'confirmation.html',param)






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