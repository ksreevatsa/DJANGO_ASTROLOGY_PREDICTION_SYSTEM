from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home.html'),
    path("",views.home,name="home"),
    path("register",views.registration,name="register"),
    path("login",views.login,name="login"),
    path("checklogin",views.checklogin,name="userlogin"),
    path('feedback/',views.feedback_form, name='feedback'),
    path('userhome/',views.userhome_render, name='userhome'),
    path('checksign/',views.checksign, name='checksign'),
    path('horoscope/',views.horoscope, name='horoscope'),
    path('checkhoroscope/',views.checkhoroscope, name='checkhoroscope'),
    path('contact/',views.contactus,name="contact"),
    path('userchangepwd',views.userchangepwd,name="userchangepwd"),
    path('userupdatepwd',views.userupdatepwd,name="userupdatepwd"),
    path('report/', views.feedback_report, name='feedback_report'),
    path('logout/', views.logout_view, name='logout'),

    ]