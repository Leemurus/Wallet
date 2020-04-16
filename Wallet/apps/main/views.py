from django.shortcuts import render

from .models import Wallet, Transaction
from .utils import elements_to_json


def index(request):
    return render(
        request,
        'main.html',
        {
            'wallets': elements_to_json(Wallet.objects.all()),
            'transactions': elements_to_json(Transaction.objects.all())
        }
    )
