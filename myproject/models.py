from django.contrib import admin
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)  # Ensures no duplicate emails

    def __str__(self):
        return self.email
    
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Remove or correct 'date_subscribed' if it's not in your model
