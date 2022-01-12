"""OnlineDocumentServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from users.views import (
    CodeConfirmView,
    SignOutView,
    check_client_code,
)
from file_storage.views import (
    DashboardView,
    protected_serve
)

admin.site.site_title = 'Admin Panel'
admin.site.site_header = 'Administration'
admin.site.index_title = 'Admin Panel'

urlpatterns = [
    re_path(r'^admin_console/', admin.site.urls, name='admin_url'),
    re_path(r'^$', CodeConfirmView.as_view(), name='code_confirm'),
    re_path(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    re_path(r'^check_client_code/', check_client_code, name='check_client_code'),
    re_path(r'^sign_out/', SignOutView.as_view(), name='sign_out'),
    re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),
]

