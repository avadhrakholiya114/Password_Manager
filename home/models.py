from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class user_passsword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username_or_email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    app_type = models.CharField(max_length=100)
    website_name = models.CharField(max_length=100, blank=True)
    website_url = models.CharField(max_length=100, blank=True)
    application_name = models.CharField(max_length=50, blank=True)
    game_name = models.CharField(max_length=50, blank=True)
    other_name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        app_name = ""
        if self.website_name:
            app_name = self.website_name
        elif self.application_name:
            app_name = self.application_name
        elif self.game_name:
            app_name = self.game_name
        return f'{app_name} password'
