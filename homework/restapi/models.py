from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Store(models.Model):
    status_choice = [
        ("active", "active"),
        ("deactivated", "deactivated"),
        ("in_review", "In review"),
    ]

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    status = models.CharField(choices=status_choice, default='in_review', max_length=30)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)

