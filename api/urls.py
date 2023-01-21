from django.urls import path, include
from users.views import UserCreationApi, UserDetailApi
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('products/', include('products.urls')),
    path('carts/', include('carts.urls')),
    path('signup/', UserCreationApi.as_view()),
    path('users/<int:pk>/', UserDetailApi.as_view()),
    path('login/', obtain_auth_token)
]