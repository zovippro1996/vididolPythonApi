from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """This is a class for keeping general User Account

    Arguments:
        AbstractUser {class} -- Django Class
    """
    email = models.EmailField(
        verbose_name="User's personal email",
        max_length=200,
        unique=True)
    facebook_link = models.URLField(
        verbose_name="User's Facebook link",
        max_length=250)
    instagram_link = models.URLField(
        verbose_name="User's Instagram link",
        max_length=250)
    is_email_activated = models.BooleanField(
        verbose_name="check User email activated",
        default=False)
    last_updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class Star(User):
    """This class help identify Star Account

    Arguments:
        User {class} -- Base User Class
    """
    is_certified = models.BooleanField(
        verbose_name="Check Star's certified",
        default=False)
    response_rate = models.FloatField(
        verbose_name="Star's Response Rate",
        null=True)


class UserInformation(models.Model):
    """This class provide details about User

    Arguments:
        models {class} -- default inheritent of DJango Model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(
        verbose_name="User's Fullname",
        max_length=250)
    avatarlocation = models.URLField(
        verbose_name="User's Avatar path",
        max_length=250)
    phonenumber = models.CharField(
        verbose_name="User's Phone Number",
        max_length=250)
    description_bio = models.CharField(
        verbose_name="User's Description or Bio",
        max_length=1000)
    last_updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)