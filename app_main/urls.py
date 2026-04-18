from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('home/', views.home, name="home"),
    path('transactions/', views.transactions, name="transactions"),
    path('recurring/', views.recurring, name="recurring"),
    path('analytics/', views.analytics, name="analytics"),
    path('chat/', views.chat, name="chat"),
    path('budgets/', views.budgets, name="budgets"),
    path('scan-receipt/', views.scan_receipt, name="scan_receipt"),
]
