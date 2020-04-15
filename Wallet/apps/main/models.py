from django.db import models


class Wallet(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=1000, decimal_places=15)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=1000, decimal_places=15)
    comment = models.CharField(max_length=100)
    date = models.DateTimeField()
