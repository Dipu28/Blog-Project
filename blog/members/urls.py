from django.urls import path
from . import views as user_view


urlpatterns = [
    path('register/',user_view.UserRegisterView.as_view(),name='register'),
]
