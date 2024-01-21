from django.contrib import admin
from .models import Exchange, Ticker, Sentiment

admin.site.register(Exchange)
admin.site.register(Ticker)
admin.site.register(Sentiment)
