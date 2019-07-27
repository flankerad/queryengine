from django.test import TestCase, Client
from django.urls import reverse
from ..models import Analytics

client = Client()


class AnalyticsAPITestCase(TestCase):
    '''
        Test module for API
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

    def test_get_api(self):
        response = client.get(
            reverse('data_analytics'),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test