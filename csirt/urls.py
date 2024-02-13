"""
URL configuration for csirt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views import generic
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from csirt.settings_utils import get_env_variable

admin.site.site_header = "CSIRT"
admin.site.site_title = "CSIRT Admin Portal"
admin.site.index_title = "Welcome to CSIRT Portal"

schema_view = get_schema_view(
    openapi.Info(
        title="CSIRT API Documentation",
        default_version="v1",
        description=(
            "This is a collection of all available APIs for "
            "the CSIRTs System"
        ),
        terms_of_service="http://localhost/",
        contact=openapi.Contact(email="cms@CSIRT.com"),
        license=openapi.License(name="BSD License"),
    ),
    url=get_env_variable("DEFAULT_URL", "https://acms-api.CSIRT-dev.net/"),
    public=True,
    # permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
       path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", generic.RedirectView.as_view(url="/docs/", permanent=False)),
]
