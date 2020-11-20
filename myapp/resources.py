from import_export import resources
from .models import *

class AccountsGeneralledgerResource(resources.ModelResource):
    class Meta:
        model =AccountsGeneralledger
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields =(
            'label',
            'notes',
            'payer_name',
            'receiver_name',
            'entry_type',
            'transaction_date',
            'amount',
            'created_at',
            'updated_at',
            'account_type_id',
            'asset_id',
            'attachment_id',
            'created_by_id',
            'reviewer_id',
            'updated_by_id',
            'user_id',
            'currency_id',
            'lease_transaction_id',
            'payment_transaction_id',
            'sale_transaction_id'

        )


class AccountsGeneralledgerHistoryResource(resources.ModelResource):
    class Meta:
        model =AccountsGeneralledgerHistory
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields =(
            'label',
            'notes',
            'payer_name',
            'receiver_name',
            'entry_type',
            'transaction_date',
            'amount',
            'created_at',
            'updated_at',
            'history_id',
            'history_date',
            'history_change_reason',
            'history_type',
            'account_type_id',
            'asset_id',
            'attachment_id',
            'created_by_id',
            'history_user_id',
            'reviewer_id',
            'updated_by_id',
            'user_id',
            'currency_id',
            'lease_transaction_id',
            'payment_transaction_id',
            'sale_transaction_id'

        )