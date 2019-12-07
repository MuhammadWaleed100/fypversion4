from django.urls import path
from . import views


urlpatterns = [
    path('',views.base, name='base.html'),
    path('contact/',views.contact, name='contact.html'),
    path('newpost/',views.newpost, name='new-post.html'),
    path('wantajob/',views.wantajob, name='job-post.html'),
    path('login/',views.login, name='login.html'),
    path('signup/',views.signup, name='signup.html'),
    path('register/',views.register, name='signup.html'),
    path('userlogin/',views.userlogin, name='login.html'),
    path('profile/',views.profile, name='profile.html'),
    path('forget/', views.forget, name='forget'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('confirmm/', views.confirmm, name='confirmm'),
]
