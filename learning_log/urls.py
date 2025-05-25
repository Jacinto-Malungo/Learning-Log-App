from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
]
