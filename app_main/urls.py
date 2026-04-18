from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('process_receipt_image/', views.process_receipt_image, name="process_receipt_image"),

]
