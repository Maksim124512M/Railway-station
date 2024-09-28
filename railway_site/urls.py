from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls', namespace='users')),
    path('', include('railway_system.urls', namespace='railway_system')),
]
