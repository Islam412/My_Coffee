from django.urls import path
from . import views

urlpatterns = [
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
]