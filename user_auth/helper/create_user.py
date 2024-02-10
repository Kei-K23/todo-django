from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


def create_user(username, password, email=None, first_name=None, last_name=None):
    user = User.objects.create_user(
        username=username, password=password, email=email,
        first_name=first_name, last_name=last_name)
    return user
