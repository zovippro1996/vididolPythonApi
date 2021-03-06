# Generated by Django 3.0.6 on 2020-06-10 17:11

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import webserviceapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('account_facebook_link', models.URLField(max_length=250, verbose_name="User's Facebook link")),
                ('account_instagram_link', models.URLField(max_length=250, verbose_name="User's Instagram link")),
                ('account_is_email_activated', models.BooleanField(default=False, verbose_name='check User email activated')),
                ('account_is_star', models.BooleanField(default=False, verbose_name='User is Star or Not')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_description', models.CharField(max_length=2056, verbose_name='Log description')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('star_is_certified', models.BooleanField(default=False, verbose_name="Check Star's certified")),
                ('star_response_rate', models.FloatField(null=True, verbose_name="Star's Response Rate")),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('webserviceapi.account',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='original Account')),
                ('userinformation_fullname', models.CharField(max_length=250, verbose_name="User's Fullname")),
                ('userinformation_avatarlocation', models.URLField(max_length=250, verbose_name="User's Avatar path")),
                ('userinformation_phonenumber', models.CharField(max_length=250, verbose_name="User's Phone Number")),
                ('userinformation_description_bio', models.CharField(max_length=1000, verbose_name="User's Description or Bio")),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(upload_to=webserviceapi.models.user_directory_path, verbose_name='Video File URL')),
                ('video_duration', models.DurationField(verbose_name='Video duration')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account that has full privilege on the Video')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=256, verbose_name='Content of the comment')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
                ('comment_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner of the comment')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_description', models.CharField(max_length=500, verbose_name='Description of the Post')),
                ('post_is_private', models.BooleanField(default=False, verbose_name='Hide or public post')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
                ('post_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner of the post')),
                ('post_videos', models.ManyToManyField(to='webserviceapi.Video', verbose_name='Videos of Post')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_content', models.CharField(max_length=500, verbose_name='description')),
                ('notification_link', models.URLField(max_length=500, verbose_name='link to details')),
                ('notification_is_read', models.BooleanField(default=False, verbose_name='Check if the notification is Read')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
                ('notification_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User receives the notification')),
            ],
        ),
        migrations.CreateModel(
            name='VideoLengthOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videolengthoption_time', models.DurationField(verbose_name='Duration of the Video')),
                ('videolengthoption_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price for the Video Length')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
                ('videolengthoption_star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webserviceapi.Star')),
            ],
        ),
        migrations.CreateModel(
            name='FanRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_content', models.CharField(max_length=250, verbose_name='Message from User')),
                ('request_status', models.CharField(choices=[('NEW', 'Mới'), ('DRAFT', 'Lưu nội bộ'), ('SENT', 'Đã gửi'), ('ACCEPTED', 'Đã chấp nhận'), ('WAITING', 'Đang xử lí clip'), ('REJECTED', 'Đã từ chối'), ('CANCELED', 'Đã hủy bỏ'), ('DONE', 'Hoàn tất')], default='NEW', max_length=10)),
                ('request_is_read', models.BooleanField()),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Logging record last changed time')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Logging record created time')),
                ('request_owner_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_from', to=settings.AUTH_USER_MODEL, verbose_name='Account sends the request')),
                ('request_star_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_to', to='webserviceapi.Star', verbose_name='Star receives the request')),
            ],
        ),
    ]
