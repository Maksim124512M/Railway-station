from django.db import models
from django.urls import reverse


class TimeTable(models.Model):
    route = models.CharField(max_length=255)
    depature_date = models.DateTimeField()
    date_of_arrival = models.DateTimeField()
    price_of_ticket = models.IntegerField()
    total_tickets = models.IntegerField(default=30)
    date_of_appointment = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('railway_system:book_ticket', kwargs={
            'timetable_id': self.id,
        })

    def count_tickets(self):
        self.total_tickets -= 1

    def __str__(self):
        return 'Потяг за розкладом ' + self.route
    
    class Meta:
        verbose_name = 'Розклад'
        verbose_name_plural = 'Розклади'


class BookTicket(models.Model):
    table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'Бронь квитка на {self.table}'

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Броні'    
