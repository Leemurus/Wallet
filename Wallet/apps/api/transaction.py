from datetime import datetime
import json

from main.models import Wallet, Transaction
from django.http import HttpResponse, HttpResponseServerError


def add_transaction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            wallet_title = str(json_data['wallet_title'])
            amount = json_data['amount']
            comment = str(json_data['comment'])

            wallets = Transaction.objects.filter(title=wallet_title)
            if not isinstance(amount, float) or len(wallets) == 0:
                raise ValueError()


            Transaction(
                wallet=wallets[0],
                title=wallet_title,
                amount=amount,
                date=datetime.utcnow(),
                comment=comment,
            ).save()
        except KeyError or ValueError or Wallet.DoesNotExist:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(
            json.dumps('Ok'),
            content_type='application/json'
        )

    return HttpResponse()


def delete_transaction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']

            wallet = Wallet.objects.get(id=id)
            if not isinstance(id, int):
                raise ValueError()

            wallet.delete()
        except KeyError or ValueError or Wallet.DoesNotExist:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(
            json.dumps('Ok'),
            content_type='application/json'
        )

    return HttpResponse()


def get_transactions_by_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            wallet_title = str(json_data['wallet_title'])
            wallet = Wallet.objects.filter(title=wallet_title)[0]
        except KeyError:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(
            json.dumps(list(wallet.transaction_set.all())),
            content_type='application/json'
        )

    return HttpResponse()


def get_all_transactions(request):
    return HttpResponse(
        json.dumps(list(Wallet.objects.all())),
        content_type='application/json'
    )
