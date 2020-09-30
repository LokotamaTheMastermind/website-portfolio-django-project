from django.urls import path
from .views import *

app_name = 'policies'

urlpatterns = [
    path('privacy/', privacy, name='privacy-policy'),
    path('terms-conditions/', terms_conditions, name='terms-and-conditions')
]
