from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15)
    invite_code_active = models.CharField(max_length=6)
    invite_code_personal = models.CharField(max_length=6)
