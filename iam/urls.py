from django.urls import path
from iam.views import login

urlpatterns = [
    path('login/', login, name='login')
]
