

# 📘 Project Documentation: **StockNepal (Live Market Tracking App)**

## 📁 Project Setup

### 1. Create Project Directory

```bash
mkdir StockNepal
cd StockNepal

```

### 2. Create a Virtual Environment

```bash
python -m venv venv

```

### 3. Activate the Virtual Environment

-   **Windows**:
    

```bash
venv\Scripts\activate

```

-   **macOS/Linux**:
    

```bash
source venv/bin/activate

```

### 4. Install Django

```bash
pip install django

```

### 5. Create a Django Project

```bash
django-admin startproject StockNepal .

```

> The `.` at the end ensures the project files are created in the current directory.

### 6. Run the Development Server (to verify setup)

```bash
python manage.py runserver

```

You should see:

```
Starting development server at http://127.0.0.1:8000/

```

----------

## 🧩 Create a Django App: `livemarket`
### Ref:
## Python script to fetch and parse the live trading data from the URL:

    
    import requests
    import json
    
    # URL of the data source
    url = "https://www.onlinekhabar.com/smtm/stock_live/live-trading"
    
    # Fetching the data
    
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            # Extract the list of stock data
            stocks = data.get("response", [])
            
            # Print all stock data in a formatted way
            for stock in stocks:
                print(f"Ticker: {stock['ticker']}")
                print(f"Name: {stock['ticker_name']}")
                print(f"Index: {stock['indices']}")
                print(f"LTP: {stock['ltp']}")
                print(f"Volume: {stock['volume']}")
                print(f"Change: {stock['point_change']} ({stock['percentage_change']}%)")
                print(f"Open: {stock['open']}, High: {stock['high']}, Low: {stock['low']}")
                print(f"Previous Close: {stock['previousClosing']}")
                print(f"Amount: {stock['amount']}")
                print(f"Last Updated: {stock['calculated_on']}")
                print(f"Logo URL: https://{stock['icon']}")
                print('-' * 60)
        else:
            print("Failed to retrieve data. Status code:", response.status_code)


### 7. Start the App

```bash
python manage.py startapp livemarket

```

----------

## ⚙️ Configure the App in Django Settings

### 8. Open `StockNepal/settings.py` and locate `INSTALLED_APPS`. Add `'livemarket',` to the list.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livemarket',  # <- Add this line
]

```

----------

## 🚀 Run the Server Again

```bash
python manage.py runserver

```

You can now start building your live stock market tracking features inside the `livemarket` app.





----------

### 🛠 Step 1: Define the Model to Store Stock Data

In your `livemarket` app, open the `models.py` file and define the following model to store stock data.

#### `livemarket/models.py`

```python
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

```

### 🧰 Step 2: Migrate the Database

Once you've defined your model, you need to create the database tables.

Run the following commands:

```bash
python manage.py makemigrations livemarket
python manage.py migrate

```

----------

### 🧑‍💻 Step 3: Fetch Data and Update Database

Now, create a view that will fetch data from the URL, update the database, and display it in `stocks.html`.

#### `livemarket/views.py`

```python
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

```

----------

### 🏗 Step 4: Create a Template to Display the Stock Data

Create a new folder `templates/livemarket` in your `livemarket` app directory. Inside that, create the `stocks.html` template.

#### `livemarket/templates/livemarket/stocks.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock Nepal</title>
</head>
<body>
    <h1>Stock Live Market Data</h1>

    <table border="1">
        <thead>
            <tr>
                <th>Ticker</th>
                <th>Name</th>
                <th>Index</th>
                <th>LTP</th>
                <th>Volume</th>
                <th>Change</th>
                <th>Open</th>
                <th>High</th>
                <th>Low</th>
                <th>Previous Close</th>
                <th>Amount</th>
                <th>Last Updated</th>
                <th>Logo</th>
            </tr>
        </thead>
        <tbody>
            {% for stock in stocks %}
                <tr>
                    <td>{{ stock.ticker }}</td>
                    <td>{{ stock.ticker_name }}</td>
                    <td>{{ stock.indices }}</td>
                    <td>{{ stock.ltp }}</td>
                    <td>{{ stock.volume }}</td>
                    <td>{{ stock.point_change }} ({{ stock.percentage_change }}%)</td>
                    <td>{{ stock.open_price }}</td>
                    <td>{{ stock.high }}</td>
                    <td>{{ stock.low }}</td>
                    <td>{{ stock.previous_closing }}</td>
                    <td>{{ stock.amount }}</td>
                    <td>{{ stock.last_updated }}</td>
                    <td><img src="{{ stock.logo_url }}" alt="{{ stock.ticker }}" width="50"></td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

```

----------

### 📝 Step 5: Set Up URL for the View

Create a `urls.py` file in the `livemarket` app if it doesn't exist, and add the URL configuration for the stock data view.

#### `livemarket/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_view, name='stock_view'),
]

```

Then, include this app's URL configuration in the project's main `urls.py`.

#### `StockNepal/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livemarket/', include('livemarket.urls')),
]

```

----------

### 🏁 Step 6: Run the Development Server

Now, run the Django development server again:

```bash
python manage.py runserver

```

----------

### 📱 Step 7: View the Stock Data

Go to the URL:

```
http://127.0.0.1:8000/livemarket/

```

You should now see the live stock data displayed in a table, and each time you reload the page, the data will be fetched and updated in the database.
