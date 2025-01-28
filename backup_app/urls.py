from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_backup, name='create_backup'),
    path('add-data/', views.add_test_data, name='add_test_data'),
]