from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from dash.views import (
    dash_view,
    task1_endpoint,
    task2_endpoint,
    task3_endpoint,
    process_log_view,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', dash_view, name='dashboard'),
    path('task1/<file_name>', task1_endpoint, name='task1'),
    path('task2/<file_name>', task2_endpoint, name='task2'),
    path('task3/<file_name>', task3_endpoint, name='task3'),
    path('logs', process_log_view, name='process_log'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)