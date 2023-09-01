from django.urls import path
from .views import login_view, logout_view, register_view
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register_view, name='signup'),
    path('myapp/home/', views.home, name='home'),
    path('index/', views.index, name='index'),
]