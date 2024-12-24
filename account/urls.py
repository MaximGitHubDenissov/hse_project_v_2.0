from django.urls import path
from .views import login_view, register
from django.contrib.auth import views as auth_views
    
urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]