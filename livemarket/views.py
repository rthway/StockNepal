import requests
from django.shortcuts import render
from django.utils import timezone
from .models import Stock

# URL of the data source
url = "https://www.onlinekhabar.com/smtm/stock_live/live-trading"

def fetch_and_update_stocks():
    # Fetching the data
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stocks = data.get("response", [])
        
        # Replace old data with new data
        Stock.objects.all().delete()  # Remove previous records

        for stock in stocks:
            Stock.objects.create(
                ticker=stock['ticker'],
                ticker_name=stock['ticker_name'],
                indices=stock['indices'],
                ltp=stock['ltp'],
                volume=stock['volume'],
                point_change=stock['point_change'],
                percentage_change=stock['percentage_change'],
                open_price=stock['open'],
                high=stock['high'],
                low=stock['low'],
                previous_closing=stock['previousClosing'],
                amount=stock['amount'],
                last_updated=timezone.now(),
                logo_url=f"https://{stock['icon']}"
            )

def stock_view(request):
    fetch_and_update_stocks()  # Fetch and update data every time the page is loaded

    # Get all stocks from the database
    stocks = Stock.objects.all()
    
    return render(request, 'livemarket/stocks.html', {'stocks': stocks})
