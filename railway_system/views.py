from django.views import generic
from django.urls import reverse_lazy

from railway_system.models import TimeTable, BookTicket


class HomeView(generic.ListView):
    template_name = 'railway_system/home.html'
    model = TimeTable
    context_object_name = 'timetables'


class BookTicketView(generic.CreateView):
    model = BookTicket
    fields = ['first_name', 'last_name', 'phone_number', 'email']
    template_name = 'railway_system/book_ticket.html'
    success_url = reverse_lazy('railway_system:home')

    def form_valid(self, form):
        table = TimeTable.objects.get(id=self.kwargs.get('timetable_id'))
        table.count_tickets()
        table.save()
        
        form.instance.table = table
        form.save()

        return super().form_valid(form)