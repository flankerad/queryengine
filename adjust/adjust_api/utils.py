import csv
import logging
from datetime import datetime
from .models import Analytics
from django.db.models import Q, Sum, Count, Avg, ExpressionWrapper, FloatField, F
from functools import reduce
import operator

logger = logging.getLogger(__name__)

def insert_data():
    with open('../sampledata.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            obj, created = Analytics.objects.get_or_create(
                date = datetime.strptime(row[0].replace('.', '-'), '%d-%m-%Y'),
                channel = row[1].strip().lower(),
                country = row[2].strip().lower(),
                os = row[3].strip().lower(),
                impressions = row[4],
                clicks = row[5],
                installs = row[6],
                spend = row[7],
                revenue = row[8]
            )


def get_filtered_result(qp):
    '''
        Create fitler expressions
        Return filtered results
    '''
    filters = [ 'date_to', 
                'date_from',
                'date',
                'channel',
                'country',
                'os',
                'impression',
                'clicks',
                'installs',
                'spend',
                'revenue']

    lookup_exp = {
        'date_to': 'date__lte',
        'date_from': 'date__gte'
    }
    kwargs = {}
        
    '''
        Get the filters in query params
        Check for filters with lookup exp
    '''
    for f in filters:
        if f in qp:

            if f in lookup_exp:
                f_key = lookup_exp[f]
            else:
                f_key = f

            kwargs[f_key] = qp.get(f)

    return Analytics.objects.filter(**kwargs)

def calculate_cpi(queryset):
    '''
        Calculate CPI
        cpi = spend / installs
    '''
    return queryset.annotate(cpi=Sum(ExpressionWrapper(F('spend')/F('installs'), output_field=FloatField())))     

def get_sorted_result(queryset, qp, **kwargs):
    '''
        Return a sorted queryset
    '''
    order = qp.get('order','') 
    sortby = qp.get('sortby')

    if sortby in kwargs:
        sortby = order + kwargs[qp.get('sortby')]

    return queryset.order_by(sortby)


def get_annotate_result(queryset, qp):
    '''
        Return annotation result of queryset
    '''

    annotate_func = {
        'sum': Sum,
        'count': Count,
        'avg': Avg,
    }
    annotate_exp = []
    sort_dict = {}

    '''
        Check if there are annotation keys in query params
        Create annotation expression
    '''
    if set(qp).intersection(annotate_func): 

        for key in annotate_func.keys():
            if qp.get(key):

                values = qp.get(key).split(',')
                
                if 'cpi' in values: # remove cpi from aggregation, already calculated
                    values.remove('cpi')
                
                # Create annotation expression, from query params
                annotate_exp.append([annotate_func[key](field) for field in values])
                '''
                    Create a sort dict for annotated keys
                    Eg: Sum('revenue') -> 'revenue__sum' 
                '''
                for f in values:
                    sort_dict[f] = f + "__" + key 

              
        queryset = queryset.annotate(*reduce(operator.add, annotate_exp))
    
    return queryset, sort_dict