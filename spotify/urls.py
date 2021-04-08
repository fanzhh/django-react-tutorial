from django.urls import path
from .views import AuthURL

urlpatterns = [
    path('/get_auth-url', AuthURL.as_view()),
]
