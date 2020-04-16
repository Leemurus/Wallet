import json
import decimal
from django.http import HttpResponse, HttpResponseServerError
from django.utils import timezone

from main.models import Wallet, Transaction
from main.utils import list_to_json


def add_transaction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            wallet_title = str(json_data['wallet_title'])
            amount_str = str(json_data['amount'])
            comment = str(json_data['comment'])
            wallet = Wallet.get_wallet(wallet_title)

            if not amount_str.replace('.', '', 1).isdigit():
                raise ValueError('Amount must be float type')
            if wallet is None:
                raise ValueError('Wallet name is incorrect')
            if decimal.Decimal(amount_str) == 0:
                raise ValueError('Amount must be less than or greater than 0')

            wallet.add_transaction(
                wallet=wallet, amount=decimal.Decimal(amount_str),
                date=timezone.now(), comment=comment
            )
        except KeyError:
            return HttpResponseServerError('Incorrect data')
        except ValueError as e:
            return HttpResponseServerError(e.args[0])

        return HttpResponse(json.dumps('Ok'), content_type='application/json')


def delete_transaction(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']

            if not isinstance(id, int):
                raise ValueError()

            transaction = Transaction.objects.get(id=id)
            transaction.wallet.delete_transaction(transaction)
        except KeyError:
            return HttpResponseServerError('Incorrect data')
        except ValueError:
            return HttpResponseServerError('Id must be integer type')
        except Transaction.DoesNotExist:
            return HttpResponseServerError('This transaction does not exist')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')


def get_transactions_by_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']

            if not isinstance(id, int):
                raise ValueError()

            wallet = Wallet.objects.get(id=id)
        except KeyError:
            return HttpResponseServerError('Incorrect data')
        except ValueError:
            return HttpResponseServerError('Id must be integer type')
        except Wallet.DoesNotExist:
            return HttpResponseServerError('This wallet does not exist')

        return HttpResponse(list_to_json(wallet.transaction_set.all()),
                            content_type='application/json')


def get_all_transactions(request):
    return HttpResponse(
        list_to_json(Transaction.objects.all()),
        content_type='application/json'
    )
