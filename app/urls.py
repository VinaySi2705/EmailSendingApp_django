from . views import EmailView
from django.urls import path

urlpatterns = [
    path('', EmailView.as_view(), name='email')
]
