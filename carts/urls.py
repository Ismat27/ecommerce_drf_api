from django.urls import path
from .views import (CartRetrieveUpdate)

urlpatterns = [
    path('<int:pk>/', CartRetrieveUpdate.as_view())
]