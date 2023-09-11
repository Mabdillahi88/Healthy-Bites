# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
from datetime import datetime
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestBookingsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.reservation_request_url = reverse('user_reservation_request_view')
        self.acknowledgment_url = reverse('booking_acknowledgment_page_view')
        self.dashboard_url = reverse('user_specific_bookings_dashboard_view')
        self.booking = Booking.objects.create(user=self.user, requested_date=datetime.now(), status="Pending")
        self.modify_url = reverse('individual_booking_modification_view', kwargs={'pk': self.booking.pk})
        self.terminate_url = reverse('specific_booking_termination_view', kwargs={'pk': self.booking.pk})

    def test_reservation_request_GET(self):
        response = self.client.get(self.reservation_request_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'initiate_reservation_page.html')

    def test_acknowledgment_GET(self):
        response = self.client.get(self.acknowledgment_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'acknowledgment_view.html')

    def test_dashboard_GET(self):
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'active_bookings_dashboard.html')

    def test_individual_booking_modification_view_GET(self):
        response = self.client.get(self.modify_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modify_reservation_form.html')

    def test_specific_booking_termination_view_GET(self):
        response = self.client.get(self.terminate_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'terminate_reservation_dialog.html')

    def test_specific_booking_termination_view_POST_delete(self):
        response = self.client.post(self.terminate_url)
        self.assertEqual(response.status_code, 302)  # expect a redirect after delete
        self.assertFalse(Booking.objects.filter(pk=self.booking.pk).exists())  # booking should no longer exist

    # Note: More comprehensive test cases would cover the form POST actions, error handling, permissions, etc.
