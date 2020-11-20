import csv
from django import forms
from io import TextIOWrapper
from .models import *



class AccountsGeneralledger(forms.ModelForm):
    class Meta:
        model = AccountsGeneralledger
        fields = ('id',
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


class CSVImportForm(forms.Form):
    filename = forms.FileField(label='Select a CSV file to import:',)

    def clean(self):
        cleaned_data = super(CSVImportForm, self).clean()


        f = TextIOWrapper(self.cleaned_data.get('filename'), encoding='ASCII')
        result_csvlist = csv.DictReader(f)
        event_info = next(result_csvlist)
        f_eventinfo = AccountsGeneralledgerForm(event_info)

        if not f_eventinfo.is_valid():
            raise forms.ValidationError("Error validating 1st line of data (after header) in CSV")
        return cleaned_data



class AccountsGeneralledgerForm(forms.Form):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    payer_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    account_type_id = models.BigIntegerField()
    asset_id = models.BigIntegerField()
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    reviewer_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    currency_id = models.IntegerField()
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)



#AccountsGeneralledgerHistory
class AccountsGeneralledgerHistory(forms.ModelForm):
    class Meta:
        model =AccountsGeneralledgerHistory
        fields = ('id',
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



def clean(self):
        cleaned_data = super(CSVImportForm, self).clean()


        f = TextIOWrapper(self.cleaned_data.get('filename'), encoding='ASCII')
        result_csvlist = csv.DictReader(f)
        event_info = next(result_csvlist)
        f_eventinfo = AccountsGeneralledgerHistoryForm(event_info)

        if not f_eventinfo.is_valid():
            raise forms.ValidationError("Error validating 1st line of data (after header) in CSV")

        return cleaned_data


class AccountsGeneralledgerHistoryForm(forms.Form):
    id = models.BigIntegerField()
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    payer_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    account_type_id = models.BigIntegerField(blank=True, null=True)
    asset_id = models.BigIntegerField(blank=True, null=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    reviewer_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)


class AccountsGeneralledgercategory(forms.ModelForm):
    class Meta:
        model =AccountsGeneralledgercategory
        fields =('id',
                   'entry_type',
                   'name',
                   'created_at',
                   'updated_at',
                   'created_by_id',
                   'updated_by_id',
                   )

def clean(self):
        cleaned_data = super(CSVImportForm, self).clean()

        f = TextIOWrapper(self.cleaned_data.get('filename'), encoding='ASCII')
        result_csvlist = csv.DictReader(f)
        event_info = next(result_csvlist)
        f_eventinfo = AccountsGeneralledgercategoryForm(event_info)

        if not f_eventinfo.is_valid():
            raise forms.ValidationError("Error validating 1st line of data (after header) in CSV")

        return cleaned_data
class AccountsGeneralledgercategory(forms.Form):
    id = models.BigAutoField(primary_key=True)
    entry_type = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

