from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm
import datetime


class UserReservationRequestView(LoginRequiredMixin, View):
    template_name = 'initiate_reservation_page.html'
    success_message = 'Booking successful, waiting.'  # Updated message

    def get_booking_form(self, request):
        initial_data = {
            'email': request.user.email
        } if request.user.is_authenticated else {}
        return BookingForm(initial=initial_data)

    def get(self, request, *args, **kwargs):
        booking_form = self.get_booking_form(request)
        return render(
            request, self.template_name, {'booking_form': booking_form}
        )  # Display the booking form

    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, self.success_message)
            return redirect('acknowledgment_view')
        return render(
            request, self.template_name, {'booking_form': booking_form}
        )


class BookingAcknowledgmentPageView(LoginRequiredMixin, View):
    template_name = 'acknowledgment_view.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UserSpecificBookingsDashboardView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'active_bookings_dashboard.html'
    paginate_by = 4
    context_object_name = 'booking'

    def get_queryset(self):
        today = datetime.datetime.now().date()
        Booking.objects.filter(
            user=self.request.user,
            requested_date__lt=today
        ).update(status='Timed Out')

        user_bookings = Booking.objects.filter(
            user=self.request.user
        ).order_by('-created_date')

        print(
            f"Bookings for user {self.request.user.username}: {user_bookings}"
        )
        return user_bookings


class IndividualBookingModificationView(
        LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'modify_reservation_form.html'
    success_message = 'Booking has been updated.'
    success_url = reverse_lazy('active_bookings_dashboard')


class SpecificBookingTerminationView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'terminate_reservation_dialog.html'
    success_message = "Booking cancelled"
    success_url = reverse_lazy('active_bookings_dashboard')

    def get_object(self, queryset=None):
        booking = get_object_or_404(Booking, pk=self.kwargs['pk'])
        if booking.user != self.request.user and not self.request.user.is_superuser:  # noqa
            raise PermissionDenied(
                "You don't have permission to cancel this booking."
            )
        return booking

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().delete(request, *args, **kwargs)
