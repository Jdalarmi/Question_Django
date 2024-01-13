from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name="home-page"),
    path('confirmation/',views.confimation_request, name='confirmation')
]
