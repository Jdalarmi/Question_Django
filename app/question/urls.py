from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_user_test, name="home-page"),
    path('confirmation/',views.confimation_request, name='confirmation')
]
