# from django.shortcuts import render
import json
import logging
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from adjust_api.models import Analytics
from .utils import get_annotate_result


logger = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
def data_analytics(request):
    '''
        Filter, group and sort data
    '''
    if request.method == 'GET':

        try:    
            qp = request.GET.dict()
            filters = ['date_from',
                        'date_to',
                        'channel',
                        'country',
                        'os',
                        'impression',
                        'clicks',
                        'installs',
                        'spends',
                        'revenue']
            kwargs = {}

            for f in filters:
                if f in qp:
                    kwargs[f] = qp.get(f)

            queryset = Analytics.objects.filters(**kwargs)

            if qp.get('values'):
                queryset = get_annotate_result(queryset, qp)
                result = serializers.serialize(json, queryset)
        
        except ValueError as e:
            logger.error(e.msg)

        return JsonResponse({'result': result})