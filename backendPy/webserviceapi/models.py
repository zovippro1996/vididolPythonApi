from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """This is a class for keeping general User Account

    Arguments:
        AbstractUser {class} -- Django Class
    """
    email = models.EmailField(
        verbose_name="User's personal email", max_length=200, unique=True)
    facebook_link = models.URLField(
        verbose_name="User's Facebook link", max_length=250)
    instagram_link = models.URLField(
        verbose_name="User's Instagram link", max_length=250)
    is_email_activated = models.BooleanField(
        verbose_name="check User email activated", default=False)
    last_updated_time = models.DateTimeField(
        verbose_name="time User record last changed", auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="time User record created", auto_now_add=True)


class Star(User):
    """This class help identify Star Account

    Arguments:
        User {class} -- Base User Class
    """
    is_certified = models.BooleanField(
        verbose_name="check Star's certified", default=False)
    response_rate = models.FloatField(
        verbose_name="Star's Response Rate", null=True)
