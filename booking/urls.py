from django.urls import path
# Internal:
from booking import views

urlpatterns = [
    path(
        'initiate_reservation_page',
        views.UserReservationRequestView.as_view(),
        name='initiate_reservation_page'
    ),
    path(
        'acknowledgment_view',
        views.BookingAcknowledgmentPageView.as_view(),
        name='acknowledgment_view'
    ),
    path(
        'active_bookings_dashboard',
        views.UserSpecificBookingsDashboardView.as_view(),
        name='active_bookings_dashboard'
    ),
    path(
        'modify_reservation_form/<int:pk>',
        views.IndividualBookingModificationView.as_view(),
        name='modify_reservation_form'
    ),
    path(
        'terminate_reservation_dialog/<int:pk>',
        views.SpecificBookingTerminationView.as_view(),
        name='terminate_reservation_dialog'
    ),
]
