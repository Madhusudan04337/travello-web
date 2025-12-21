"""
URL configuration for travello_web project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views

urlpatterns = [
    path('',include('places.urls')),
    path('login/', account_views.login_user, name='login'),
    path('register/', account_views.register, name='register'),
    path('logout/', account_views.logout_user, name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)