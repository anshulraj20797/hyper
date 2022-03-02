from django.urls import path
from api import views


urlpatterns = [
    path('customer/',views.Customer_LC_API.as_view()),
    path('customer/<int:pk>',views.Customer_RUD_API.as_view()),
]
