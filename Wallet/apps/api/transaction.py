import json
from django.http import HttpResponse, HttpResponseServerError
from django.utils import timezone

from main.models import Wallet, Transaction
from main.utils import list_to_json


def add_transaction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            wallet_title = str(json_data['wallet_title'])
            amount = json_data['amount']
            comment = str(json_data['comment'])
            wallet = Wallet.get_wallet(wallet_title)

            if not isinstance(amount, int) or wallet is None:
                raise ValueError()

            wallet.add_transaction(
                wallet=wallet, amount=amount,
                date=timezone.now(), comment=comment
            )
        except KeyError and ValueError:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')

    return HttpResponse()


def delete_transaction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']

            if not isinstance(id, int):
                raise ValueError()

            Wallet.objects.get(id=id).delete()
        except KeyError and ValueError and Wallet.DoesNotExist:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')

    return HttpResponse()


def get_transactions_by_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']

            if not isinstance(id, int):
                raise ValueError()

            wallet = Wallet.objects.get(id=id)
        except KeyError and ValueError:
            return HttpResponseServerError('Incorrect data')
        else:
            return HttpResponse(
                list_to_json(wallet.transaction_set.all()),
                content_type='application/json'
            )

    return HttpResponse()


def get_all_transactions(request):
    return HttpResponse(
        list_to_json(Transaction.objects.all()),
        content_type='application/json'
    )
