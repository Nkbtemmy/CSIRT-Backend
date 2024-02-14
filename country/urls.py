from django.urls import path
from country import views

urlpatterns = [
    path('', views.CountryListCreate.as_view(), name='country_list_create'),
    path('<int:pk>/', views.CountryRetrieveUpdateDestroy.as_view(), name='country_retrieve_update_destroy'),
]
