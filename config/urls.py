from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from config import views


schema_view = get_schema_view(
    openapi.Info(
        title="Investment Buddy API",
        default_version="v1",
        description="Investment Buddy API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=None,
)

urlpatterns = [
    # Swagger docs
    path("swaggerxyz-docs", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-schema-ui",),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # health check
    path("", views.api_ok, name="api-ok"),
    path("v1/health-check", views.HealthCheckView.as_view(), name="health-check"),

    # admin
    path("ajazzinauth23qwe/", admin.site.urls),

    # project urls
    path('api/auth/', include('core.urls.auth')),
]
