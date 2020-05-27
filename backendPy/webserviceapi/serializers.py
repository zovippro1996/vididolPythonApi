from django.contrib.auth.models import User
from rest_framework import serializers
from backendPy.webserviceapi.models import Account, Star, UserInformation, Video, VideoLengthOptions, FanRequest, Post, PostComment, Notification


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'password',
            'email',
            'is_active',
            'account_facebook_link',
            'account_instagram_link',
            'account_is_email_activated',
            'account_is_star']


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = [
            'account_ptr_id',
            'star_is_certified',
            'star_response_rate']


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = [
            'account_id',
            'userinformation_fullname',
            'userinformation_avatarlocation',
            'userinformation_phonenumber',
            'userinformation_description_bio']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'video_file',
            'video_duration',
            'owner_id']


class VideoLengthOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLengthOptions
        fields = [
            'id',
            'videolengthoption_time',
            'videolengthoption_price',
            'videolengthoption_star_id']


class FanRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FanRequest
        fields = [
            'id',
            'request_content',
            'request_status',
            'request_is_read',
            'request_owner_account_id',
            'request_star_account_id']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'post_description',
            'post_is_private',
            'post_owner_id']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = [
            'id',
            'comment_content',
            'comment_owner_id']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'notification_content',
            'notification_link',
            'notification_is_read',
            'notification_receiver_id']
