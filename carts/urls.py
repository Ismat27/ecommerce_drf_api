from django.urls import path
from .views import (CartRetrieveUpdate, AddToCartApiView)

urlpatterns = [
    path('<int:pk>/', CartRetrieveUpdate.as_view()),
    path('items/', AddToCartApiView.as_view())
]