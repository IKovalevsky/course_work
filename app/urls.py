from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend_api/', include("backend_api.urls")),
    path('accounts/',include("django.contrib.auth.urls")),
]