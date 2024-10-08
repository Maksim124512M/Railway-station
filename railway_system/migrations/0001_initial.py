# Generated by Django 5.1.1 on 2024-09-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=255)),
                ('depature_date', models.DateTimeField()),
                ('date_of_arrival', models.DateTimeField()),
                ('price_of_ticket', models.IntegerField()),
                ('total_tickets', models.IntegerField(default=30)),
                ('date_of_appointment', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Розклад',
                'verbose_name_plural': 'Розклади',
            },
        ),
    ]
