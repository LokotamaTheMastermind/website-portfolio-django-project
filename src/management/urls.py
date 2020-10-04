from django.urls import path
from .views import *

app_name = 'management'

urlpatterns = [
    path('', index, name='management-view'),
    path('create/', create, name='management-create'),
    path('delete/<int:id>', delete, name='management-delete'),
    path('update/<int:id>', update, name='management-update'),
]
