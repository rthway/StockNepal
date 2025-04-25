

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



