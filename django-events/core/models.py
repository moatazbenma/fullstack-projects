from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone








class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField("Event Date")
    time = models.TimeField("Event Time")
    event_status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class Registration(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id}, {self.event_id}"
    

