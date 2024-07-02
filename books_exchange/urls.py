from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="BOOKS EXCHANGE DOCUMENTATION",
        default_version='v1',
        description="This a books exchange documentation by Jean Correa",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@minhaapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('users.urls', namespace='users')),
    path('api/v1/', include('books.urls', namespace='books')),
    path('api/v1/', include('exchanges.urls', namespace='exchanges')),
    path('api/v1/', include('notifications.urls', namespace='notifications')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
