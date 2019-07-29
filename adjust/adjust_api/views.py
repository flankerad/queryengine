# from django.shortcuts import render
import json
import logging
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from adjust_api.models import Analytics
from adjust_api.utils import get_filtered_result, get_annotate_result,\
                            get_sorted_result, calculate_cpi
from django.core.serializers.json import DjangoJSONEncoder

logger = logging.getLogger(__name__)

def formatted_result(queryset, valueset):
    '''
        Return list of valueset 
        or get valueset out of queryset if not already
    '''
    if not valueset:
        queryset = queryset.values()

    return (list(queryset))

# Create your views here.
def data_analytics(request):
    '''
        Filter, group and sort data
    '''
    valueset = False

    if request.method == 'POST':
        body = json.loads(request.body)

        return JsonResponse(body)

    if request.method == 'GET':
        #'date_from': '2017-05-30', 'date_to': '', 'val': 'channel,country', 'sum': 'impressions, clicks', 'sortby': 'clicks', 'ord': 'desc'}

        qp = request.GET.dict()

        queryset = get_filtered_result(qp)

        if qp.get('values'):
            valueset = True
            queryset = queryset.values(*qp.get('values').split(','))

        if 'cpi' in qp.values():
            queryset = calculate_cpi(queryset)

        queryset, sort_dict = get_annotate_result(queryset, qp)
        
        if qp.get('sortby'):
            result = get_sorted_result(queryset, qp, **sort_dict)

        result = formatted_result(queryset, valueset)

    return JsonResponse({'result': result})

 