from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .billing import get_bill_data
import time

def index(request):
    return render(request, 'index.html')

def check_bill(request):
    if request.method == 'GET':
        bill_number = request.GET.get('id')
        if len(bill_number) != 0:
            year_month = time.strftime("%Y%m", time.localtime())
            bill_data = get_bill_data(bill_number, year_month)
            return JsonResponse(bill_data)
        else:
            return JsonResponse(
                {
                    'error': 'ID Pelanggan tidak valid!'
                }, status=400
            )
    else:
        return JsonResponse(
            {
                'error': 'Metode tidak diizinkan!'
            }, status=405
        )