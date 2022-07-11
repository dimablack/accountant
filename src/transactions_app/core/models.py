"""
DATABASE MODELS.
"""
from django.conf import settings
from django.db import models


class Transaction(models.Model):
    """Transaction object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.type}_{self.amount}'
