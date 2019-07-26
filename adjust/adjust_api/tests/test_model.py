import datetime
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Analytics

client = Client()

class AnalyticsTestCase(TestCase):
    '''
        Test modules for Analytics model
    '''
    def setUp(self):
        Analytics.objects.create(
            date = '2017-05-01',
            channel = 'google',
            country = 'us',
            os = 'ios',
            impressions = 2332,
            clicks = 233,
            installs = 688,
            spend = 9839.00,
            revenue = 23434
        )
        Analytics.objects.create(
            date = '2017-10-01',
            channel = 'windows',
            country = 'us',
            os = 'ios',
            impressions = 2332,
            clicks = 233,
            installs = 688,
            spend = 9839.00,
            revenue = 23434
        )


    def test_created_data(self):
        data = Analytics.objects.get(date='2017-05-01')
        self.assertEqual(
            data.date, datetime.date(2017, 5, 1)
        )
