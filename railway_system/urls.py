from django.urls import path

from railway_system.views import HomeView, BookTicketView

app_name = 'railway_system'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bookticket/<int:timetable_id>', BookTicketView.as_view(), name='book_ticket'),
]