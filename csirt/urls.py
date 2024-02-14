from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

# Define the schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="CSIRT API Documentation",
        default_version="v1",
        description="This is a collection of all available APIs for the CSIRTs System",
        terms_of_service="http://localhost/",
        contact=openapi.Contact(email="cms@CSIRT.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Swagger documentation endpoint
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # Redirect root URL to Swagger documentation
    path("", RedirectView.as_view(url="/docs/", permanent=False)),
    # Include DRF authentication URLs
    path('api-auth/', include('rest_framework.urls')),
    # Include URLs for countries app
    path("countries/", include("country.urls")),
    # Include URLs for info app
    path("info/", include("info.urls")),
]
