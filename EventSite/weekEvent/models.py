from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    posted_date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.FileField(upload_to='media')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)