from django.urls import path
from . import views

urlpatterns = [
    path('',views.Signuppage,name='signup'),
    path('login/', views.Loginpage, name='login'),
    path('home/',views.Homepage, name='home'),
    path('login/home/', views.Homepage, name='home'),
    path('logout/',views.Logoutpage,name='logout')
]
