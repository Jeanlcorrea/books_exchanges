from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/books/', include('books.urls')),
    path('api/authors/', include('authors.urls')),
    path('api/exchanges/', include('exchanges.urls')),
    path('api/notifications/', include('notifications.urls'))
]
