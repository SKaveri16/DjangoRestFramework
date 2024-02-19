from django.test import TestCase
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer

class InvoiceTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):