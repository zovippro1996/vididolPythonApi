from django.urls import path
from webserviceapi import views
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("stars/", views.star_list),
    path("stars/<int:pk>/", views.star_detail),
    path("fanrequest/", views.fanrequest_list),
    path("fanrequest/<int:pk>/", views.fanrequest_detail),
    path("user_signin/", views.user_signin),
    path("user_signup/", views.user_signup),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Vididol API",
        description="API",
        version="1.0.2"
    ), name='openapi-schema')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
