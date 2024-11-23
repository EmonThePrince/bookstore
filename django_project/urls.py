from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #admin panel
    path('admin/', admin.site.urls),
    #User management
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')), #local
    #user app
    path('',include('pages.urls')),
]
