from django.urls import path, include
from users.views import UserCreationApi, UserDetailApi

urlpatterns = [
    path('products/', include('products.urls')),
    path('carts/', include('carts.urls')),
    path('signup/', UserCreationApi.as_view()),
    path('users/<int:pk>/', UserDetailApi.as_view())
]