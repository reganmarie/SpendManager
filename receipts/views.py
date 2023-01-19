from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.


def receipt_list(request):
    receipt_list = Receipt.objects.all()
    context = {
        "receipts": receipt_list,
    }
    return render(request, "receipts/list.html", context)
