from django.urls import path
from webserviceapi import views

urlpatterns = [
    path("stars/", views.star_list),
    path("stars/<int:pk>/", views.star_detail),
    path("fanrequest/", views.fanrequest_list),
    path("fanrequest/<int:pk>/", views.fanrequest_detail)
]