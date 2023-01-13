from django.urls import path

from .views import ProductListCreate, ProductRetrieveUpdateDelete

urlpatterns = [
    path('', ProductListCreate.as_view()),
    path('<pk>/', ProductRetrieveUpdateDelete.as_view())
]