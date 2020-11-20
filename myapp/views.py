
import csv
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django.shortcuts import render
from .registry_class import ModelsRegistryHolder
from .services import add_classes_to_server
from django.http import HttpResponse
from django.template import RequestContext



@permission_required('admin.can_add_log_entry')
def upload(request):
    template = "csv.html"


    prompt = {


    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES.get('file')
    if not csv_file:
        messages.error(request, "Please attach a csv file")
        return redirect('/upload-csv/')
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not csv file')
        return redirect('/upload-csv/')


    add_classes_to_server()
    model = ModelsRegistryHolder().get(request.POST.get('model'))
    if not model:
        messages.error(request, f"Specified model not found {request.POST.get('model')}")
        return redirect('/upload-csv/')

    try:
        model.execute(csv_file)
    except Exception as e:
        messages.error(request, f"Exception Occured - {e}")
        return redirect('/upload-csv/')
    context = {}
    return render(request, template, context)



def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="table.csv"'

    writer = csv.writer(response)
    writer.writerow([
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
            'sale_transaction_id'])

    accountsGeneralledgers = AccountsGeneralledger.objects.all().values_list( 'label',
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
            'sale_transaction_id')

    for accountsGeneralledger in accountsGeneralledgers:
        writer.writerow(accountsGeneralledger)

    return response


def models_detail(request, pk):

    obj = AccountsGeneralledger.objects.get(pk=pk)

    obj1 = AccountsGeneralledgerHistory.objects.get(pk=pk)

    context = {

        "mod1": obj,

        "mod2": obj1,

    }

    return render(request, "csv.html", context)

# Create your views here.
