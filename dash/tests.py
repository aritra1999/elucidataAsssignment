from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse

from .views import (
    dash_view,
    task1_endpoint,
    task2_endpoint,
    task3_endpoint,
    process_log_view,
)

from .models import (
    File,
    ProcessLog
)


class TestURLS(SimpleTestCase):
    def test_dashboard_url(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dash_view)


    def test_process_log_url(self):
        url = reverse('process_log')
        self.assertEquals(resolve(url).func, process_log_view)



