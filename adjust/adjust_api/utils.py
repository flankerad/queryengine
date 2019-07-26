import csv
import logging
from datetime import datetime
from .models import Analytics
'''
    date	channel	country	os	impressions	clicks	installs	spend	revenue
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