from django.urls import path
from webserviceapi import views
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("stars/", views.star_list),
    path("stars/<int:pk>/", views.star_detail),
    path("fanrequest/", views.fanrequest_list),
    path("fanrequest/<int:pk>/", views.fanrequest_detail),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema')
]
