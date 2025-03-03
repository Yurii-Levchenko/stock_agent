from celery import shared_task
import time

@shared_task
def fetch_stock_data():
    time.sleep(5)
    return "Stock data fetched successfully!"

@shared_task
def scrape_stock_data():
    # Logic to scrape stock data
    pass

@shared_task
def scrape_news():
    # Logic to scrape news articles
    pass