from django.urls import path
from info import views

urlpatterns = [
    path('', views.CERTListCreate.as_view(), name='cert_list_create'),
    path('<int:pk>/', views.CRERTRetrieveUpdateDestroy.as_view(), name='cert_retrieve_update_destroy'),
]
