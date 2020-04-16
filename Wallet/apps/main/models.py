from django.db import models


class Wallet(models.Model):
    title = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=1000, decimal_places=15, default=0.0)

    def add_transaction(self, wallet, amount, comment, date):
        transaction = Transaction(wallet=wallet, amount=amount, comment=comment, date=date)
        transaction.save()
        self.amount += transaction.amount
        self.save()

    def edit_titile(self, new_title):
        self.title = new_title
        self.save()

    @staticmethod
    def get_wallet(title):
        wallets = Wallet.objects.filter(title=title)
        if len(wallets):
            return wallets[0]
        return None

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': '{:.3f}'.format(self.amount),
        }


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=1000, decimal_places=15)
    date = models.DateTimeField()
    comment = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'amount': '{:.5f}'.format(self.amount),
            'date': str(self.date).split('.')[0],
            'comment': self.comment
        }
