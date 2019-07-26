# from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def data_analytics(request):
    '''
        Filter, group and sort data
    '''
    if request.method == 'POST':
        return JsonResponse({'name':'flanker'})
    