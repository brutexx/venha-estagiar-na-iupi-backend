from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models

class Transaction(models.Model):
    class Types(models.TextChoices):
        INCOME = "INC", "Income"
        EXPENSE = "EXP", "Expense"
    
    description = models.TextField(max_length=100)
    amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))] # Decimal() - Evitar float, para evitar arrendondamento
    )
    type = models.CharField(choices=Types, default=Types.EXPENSE)
    date = models.DateField()
    
    def __str__(self):
        return f'Description: {self.description} | Amount: {self.amount} | Type: {self.type} | Date: {self.date}'