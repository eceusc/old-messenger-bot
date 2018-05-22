from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('webhook', views.webhook, name='webhook'),
    path('confirm-email', views.confirm_email, name='confirm-email'),
]
