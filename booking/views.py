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
    success_message = 'Booking successful, awaiting confirmation.'

    def get_booking_form(self, request):
        initial_data = {'email': request.user.email} if request.user.is_authenticated else {}
        return BookingForm(initial=initial_data)

    def get(self, request, *args, **kwargs):
        booking_form = self.get_booking_form(request)
        return render(request, self.template_name, {'booking_form': booking_form})

    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, self.success_message)
            return redirect('acknowledgment_view')
        return render(request, self.template_name, {'booking_form': booking_form})