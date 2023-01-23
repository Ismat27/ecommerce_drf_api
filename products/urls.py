from django.urls import path

from .views import ProductListCreate, ProductRetrieveUpdateDelete, CategoryProduct

urlpatterns = [
    path('', ProductListCreate.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDelete.as_view()),
    path('<str:category_name>/', CategoryProduct.as_view())
]