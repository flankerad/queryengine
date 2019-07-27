import csv
import logging
import operator
from datetime import datetime
from .models import Analytics
from django.db.models import Q, Sum, Count, Avg
from functools import reduce
'''
    date channel country os	impressions	clicks installs spend revenue
'''

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
            logger.info('Created object')
            logger.info(obj)   
            print('Created object')
            print(obj)      

def calculate_cpi():
    '''
        Calculate CPI
        cpi = spend / installs
    '''

def get_annotate_result(queryset, qp):
    '''
        Get annotation results
        Map the keys from query params to annotation functions
        Create annotation expression
        Return annotationed queryset
    '''
    annotate_func = {
        'sum': Sum,
        'count': Count,
        'avg': Avg
    }
    annotate_exp = []

    for key in annotate_func.keys():
        if  qp.get(key):
            values = qp.get(key).split(',')
            annotate_exp.append([annotate_func[key](field) for field in values])

    if qp.get('sortby'):
        queryset = queryset.order_by(qp.get('sort_by'))
        return queryset.annotate(*reduce(operator.add, annotate_exp)).order_by(qp.get('sortby'))

    else:
        return queryset.annotate(*reduce(operator.add, annotate_exp)) 