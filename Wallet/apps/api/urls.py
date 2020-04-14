from django.urls import path

from . import transaction, wallet

funcs = [
    wallet.create_wallet,
    wallet.delete_wallet,
    wallet.edit_wallet,
    wallet.get_all_wallets,
    transaction.add_transaction,
    transaction.delete_transaction,
    transaction.get_transactions_by_wallet,
    transaction.get_all_transactions
]

urlpatterns = list(path(func.__name__, func, name=func.__name__) for func in funcs)
