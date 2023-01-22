from django.urls import path, include
from users.views import UserCreationApi, UserDetailApi
from users.views import UserLogin

urlpatterns = [
    path('products/', include('products.urls')),
    path('carts/', include('carts.urls')),
    path('signup/', UserCreationApi.as_view()),
    path('users/<int:pk>/', UserDetailApi.as_view()),
    path('login/', UserLogin.as_view())
]