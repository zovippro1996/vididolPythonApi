from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    """This class provide general User Account

    Arguments:
        AbstractUser {class} -- Django Class
    """
    account_facebook_link = models.URLField(
        verbose_name="User's Facebook link",
        max_length=250)
    account_instagram_link = models.URLField(
        verbose_name="User's Instagram link",
        max_length=250)
    account_is_email_activated = models.BooleanField(
        verbose_name="check User email activated",
        default=False)
    account_is_star = models.BooleanField(
        verbose_name="User is Star or Not",
        default=False)
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class Star(Account):
    """This class help identify Star Account

    Arguments:
        User {class} -- Base User Class
    """
    star_is_certified = models.BooleanField(
        verbose_name="Check Star's certified",
        default=False)
    star_response_rate = models.FloatField(
        verbose_name="Star's Response Rate",
        null=True)


class UserInformation(models.Model):
    """Provide details about User

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="original Account")
    userinformation_fullname = models.CharField(
        verbose_name="User's Fullname",
        max_length=250)
    userinformation_avatarlocation = models.URLField(
        verbose_name="User's Avatar path",
        max_length=250)
    userinformation_phonenumber = models.CharField(
        verbose_name="User's Phone Number",
        max_length=250)
    userinformation_description_bio = models.CharField(
        verbose_name="User's Description or Bio",
        max_length=1000)
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.owner.account_username, filename)


class Video(models.Model):
    """Provides details about Uploaded Video

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Account that has full privilege on the Video")
    video_file = models.FileField(
        verbose_name="Video File URL",
        upload_to=user_directory_path)
    video_duration = models.DurationField(
        verbose_name="Video duration")
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class VideoLengthOptions(models.Model):
    """Provides details about VideoLengthOptions for Stars

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    videolengthoption_star = models.ForeignKey(
        Star,
        on_delete=models.CASCADE)
    videolengthoption_time = models.DurationField(
        verbose_name="Duration of the Video")
    videolengthoption_price = models.DecimalField(
        verbose_name="Price for the Video Length",
        max_digits=10,
        decimal_places=2)
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class FanRequest(models.Model):
    """Provide details of Fan's request

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    request_owner_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="request_from",
        verbose_name="Account sends the request")
    request_star_account = models.ForeignKey(
        Star,
        on_delete=models.CASCADE,
        related_name="request_to",
        verbose_name="Star receives the request")
    request_content = models.CharField(
        verbose_name="Message from User",
        max_length=250)

    class RequestStatus(models.TextChoices):
        NEW = 'NEW', _('Mới')
        DRAFT = 'DRAFT', _('Lưu nội bộ')
        SENT = 'SENT', _('Đã gửi')
        ACCEPTED = 'ACCEPTED', _('Đã chấp nhận')
        WAITING = 'WAITING', _('Đang xử lí clip')
        REJECTED = 'REJECTED', _('Đã từ chối')
        CANCELED = 'CANCELED', _('Đã hủy bỏ')
        DONE = 'DONE', _('Hoàn tất')
    request_status = models.CharField(
        max_length=10,
        choices=RequestStatus.choices,
        default=RequestStatus.NEW)
    request_is_read = models.BooleanField()
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class Post(models.Model):
    """Provides details of Post

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    post_owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Owner of the post"
    )
    post_videos = models.ManyToManyField(
        Video,
        verbose_name="Videos of Post"
    )
    post_description = models.CharField(
        verbose_name="Description of the Post",
        max_length=500
    )
    post_is_private = models.BooleanField(
        verbose_name="Hide or public post",
        default=False,
    )
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class PostComment(models.Model):
    """Provide details about Post Comment

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    comment_owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Owner of the comment")
    comment_content = models.CharField(
        verbose_name="Content of the comment",
        max_length=256
    )
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class Notification(models.Model):
    """Provide details of Notification for User

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    notification_content = models.CharField(
        max_length=500,
        verbose_name="description"
    )
    notification_receiver = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="User receives the notification"
    )
    notification_link = models.URLField(
        max_length=500,
        verbose_name="link to details"
    )
    notification_is_read = models.BooleanField(
        verbose_name="Check if the notification is Read",
        default=False
    )
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)


class Log(models.Model):
    """Provide details of Log

    Arguments:
        models {class} -- default inheritent of Django Model
    """
    log_description = models.CharField(
        verbose_name="Log description",
        max_length=2056
    )
    updated_time = models.DateTimeField(
        verbose_name="Logging record last changed time",
        auto_now=True)
    created_time = models.DateTimeField(
        verbose_name="Logging record created time",
        auto_now_add=True)