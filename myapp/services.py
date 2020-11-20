from .registry_class import InheritableClassType
from .models import *
import csv
import io
from django.db import IntegrityError
from .exceptions import CSVException
from django import forms

class BaseCSVClass(metaclass=InheritableClassType):
    class Meta:
        name = None
        description = None
        columns = None

    @classmethod
    def info(cls):
        return {"job_name": cls.Meta.name}

    @classmethod
    def validate_headers(cls, headers):
        columns = cls.Meta.columns
        columns_str = ", ".join(columns)
        if set(columns) != set(headers):
            raise CSVException(f"Invalid Headers in CSV, Allowed headers are {columns_str}")

    @classmethod
    def read_csv(cls, csv_file):
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        data_list = [{k: v for k, v in x.items()}
                     for x in
                     csv.DictReader(io_string, skipinitialspace=True)]
        return data_list

    @classmethod
    def execute(cls, csv_file):
        data_set = cls.read_csv(csv_file)
        if data_set:
            cls.validate_headers(data_set[0].keys())
            upload = cls.upload_csv(data_set)
            return upload
        return None

    @classmethod
    def upload_csv(cls, rows):
        raise NotImplementedError("Upload CSV method not implemented")


class AccountsGeneralledgerService(BaseCSVClass):
    class Meta:
        name = "AccountsGeneralledger"
        columns = (
            'id',
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

    @classmethod
    def upload_csv(cls, rows):
        try:
            for row in rows:
                _, created = AccountsGeneralledger.objects.update_or_create(
                    id=row.get("id"),
                    label=row.get("label"),
                    notes=row.get("notes"),
                    payer_name = row.get("payer_name"),
                    receiver_name = row.get("receiver_name"),
                    entry_type = row.get("entry_type"),
                    transaction_date = row.get("transaction_date"),
                    amount = row.get("amount"),
                    created_at = row.get("created_at"),
                    updated_at = row.get("updated_at"),
                    account_type_id = row.get("account_type_id"),
                    asset_id =row.get("asset_id"),
                    attachment_id =row.get("attachment_id"),
                    created_by_id =row.get("created_by_id"),
                    reviewer_id = row.get("reviewer_id "),
                    updated_by_id = row.get("updated_by_id"),
                    user_id = row.get("user_id"),
                    currency_id =row.get("currency_id"),
                    lease_transaction_id = row.get("lease_transaction_id"),
                    payment_transaction_id =row.get("payment_transaction_id"),
                    sale_transaction_id =row.get("sale_transaction_id"),
                )
                print(_)


        except AccountsGeneralledgerHistory.DoesNotExist:
            pass

        raise forms.ValidationError("Your data saved. but some data already exists.")

def add_classes_to_server():
    AccountsGeneralledgerService()