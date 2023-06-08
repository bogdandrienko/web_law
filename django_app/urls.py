from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('recover/', views.recover),

    path('app/client/requests/', views.get_requests, name="requests"),
    path('app/client/requests/<str:pk>/', views.get_request, name="request"),  # <str:_id> - regex
]
