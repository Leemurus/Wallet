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
        except KeyError:
            return HttpResponseServerError('Incorrect data')
        except ValueError:
            return HttpResponseServerError('This name is already taken')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')


def delete_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']

            if not isinstance(id, int):
                raise ValueError()

            Wallet.objects.get(id=id).delete()
        except KeyError:
            return HttpResponseServerError('Incorrect data')
        except ValueError:
            return HttpResponseServerError('Id must be integer type')
        except Wallet.DoesNotExist:
            return HttpResponseServerError('This wallet does not exist')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')


def edit_wallet(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        try:
            id = json_data['id']
            wallet_title = str(json_data['title'])

            if not isinstance(id, int):
                raise ValueError('Id must be integer type')

            if len(Wallet.objects.filter(title=wallet_title)):
                raise ValueError('This name is already taken')

            Wallet.objects.get(id=id).edit_title(wallet_title)
        except KeyError:
            return HttpResponseServerError('Incorrect data')
        except ValueError as e:
            return HttpResponseServerError(e.args[0])
        except Wallet.DoesNotExist:
            return HttpResponseServerError('This wallet does not exist')

        return HttpResponse(json.dumps('Ok'), content_type='application/json')


def get_all_wallets(request):
    return HttpResponse(
        list_to_json(Wallet.objects.all()),
        content_type='application/json'
    )
