from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateTimeField(
        db_comment="Date and time when the transaction was published",
    )
    description = models.CharField(max_length=20, default='No Description')
    tag = models.ManyToManyField(Tag, blank=True)
    # to restraint transaction type in income or outcome
    INCOME = 'Income'
    OUTCOME = 'Outcome'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Income'),
        (OUTCOME, 'Outcome'),
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    # user_id change in user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.transaction_type} {self.amount} {self.description}"
