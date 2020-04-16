import json

from django.http import HttpResponse, HttpResponseServerError

from main.models import Wallet, Transaction
from main.utils import list_to_json


def create_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            wallet_title = str(json_data['title'])
            wallet = Wallet.get_wallet(wallet_title)

            if wallet is not None:
                raise ValueError()

            Wallet(title=wallet_title).save()
        except KeyError and ValueError:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')

    return HttpResponse()


def delete_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            wallet_title = str(json_data['wallet_title'])
            wallet = Wallet.get_wallet(wallet_title)

            if wallet is None:
                raise ValueError()

            wallet.delete()
        except KeyError and ValueError:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')

    return HttpResponse()


def edit_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            wallet_title = str(json_data['wallet_title'])
            wallet = Wallet.get_wallet(wallet_title)

            if wallet is None:
                raise ValueError()

            wallet.edit_title(wallet_title)
        except KeyError and ValueError:
            return HttpResponseServerError('Incorrect data')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')

    return HttpResponse()


def get_all_wallets(request):
    return HttpResponse(
        list_to_json(Wallet.objects.all()),
        content_type='application/json'
    )
