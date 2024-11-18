#Create a currency converter that retrieves exchange rates from different APIs concurrently. 
#Each thread can fetch data from one API, speeding up the overall conversion process

import threading
import requests

def fetch_exchange_rate(api_url, results, index):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        results[index] = data.get('rate')
    except Exception as e:
        results[index] = None
        print(f"Error fetching from {api_url}: {e}")

def currency_converter(amount, from_currency, to_currency):
    apis = [
        f"https://api1.example.com/rates?from={from_currency}&to={to_currency}",
        f"https://api2.example.com/rates?from={from_currency}&to={to_currency}",
        f"https://api3.example.com/rates?from={from_currency}&to={to_currency}"
    ]

    threads = []
    results = [None] * len(apis)

    for index, api_url in enumerate(apis):
        thread = threading.Thread(target=fetch_exchange_rate, args=(api_url, results, index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    valid_rates = [rate for rate in results if rate is not None]
    if valid_rates:
        average_rate = sum(valid_rates) / len(valid_rates)
        converted_amount = amount * average_rate
        print(f"Converted amount: {converted_amount:.2f} {to_currency}")
    else:
        print("Failed to fetch exchange rates from all APIs.")

amount = 100  
from_currency = "USD"  
to_currency = "EUR"  
currency_converter(amount, from_currency, to_currency)
