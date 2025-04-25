from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=50)
    ticker_name = models.CharField(max_length=255)
    indices = models.CharField(max_length=255)
    ltp = models.FloatField()
    volume = models.IntegerField()
    point_change = models.FloatField()
    percentage_change = models.FloatField()
    open_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    previous_closing = models.FloatField()
    amount = models.FloatField()
    last_updated = models.DateTimeField()
    logo_url = models.URLField()

    def __str__(self):
        return self.ticker
