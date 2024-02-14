from django.urls import path
from auths.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
