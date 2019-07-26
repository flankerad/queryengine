from django.db import models

# Create your models here.

class Analytics(models.Model):
    '''
        Analytics Model
        
        date | channel | country | os | impressions	| clicks | installs | spend | revenue

    '''
    date = models.DateField()
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    os = models.CharField(max_length=50)
    impressions = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    installs = models.PositiveIntegerField(default=0)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_date(self):
        return self.date