from django.db import models

# Create your models here.
class Task(models.Model):
    Priority_choices=[('high','high'),
              ('medium','medium'),
              ('low','low')]
    Status_choices=[('pending','pending'),
            ('In progress','In progress'),
            ('Completed','Completed')]

    title=models.CharField(max_length=100)
    description=models.TextField()
    priority=models.CharField(max_length=10,choices=Priority_choices)
    status=models.CharField(max_length=15,choices=Status_choices)

    def __str__(self):
        return self.title

