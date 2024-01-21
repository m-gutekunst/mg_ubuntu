from django.db import models


class Exchange(models.Model):
    exchange = models.CharField(max_length=10)

    def __str__(self):
        return self.exchange


class Ticker(models.Model):
    ticker = models.CharField(max_length=10)
    market = models.ForeignKey(Exchange, on_delete=models.CASCADE)


class Sentiment(models.Model):
    time = models.DateField()
    title = models.CharField(max_length=200)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    negative = models.DecimalField(max_digits=4, decimal_places=3)
    neutral = models.DecimalField(max_digits=4, decimal_places=3)
    positive = models.DecimalField(max_digits=4, decimal_places=3)
