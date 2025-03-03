from django.db import models

class Stock(models.Model):
    """Основна модель для збереження даних про акції."""
    symbol = models.CharField(max_length=10, unique=True)  # Наприклад, 'AAPL', 'TSLA'
    name = models.CharField(max_length=100)  # Повна назва компанії
    sector = models.CharField(max_length=50, blank=True, null=True)  # Наприклад, 'Technology'
    market_cap = models.FloatField(blank=True, null=True)  # Ринкова капіталізація
    last_price = models.FloatField(blank=True, null=True)  # Остання ціна
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.symbol} - {self.name}"

class HistoricalStockData(models.Model):
    """Збереження історичних даних про акції."""
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="historical_data")
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('stock', 'date')

    def __str__(self):
        return f"{self.stock.symbol} - {self.date}"

class StockAnalysis(models.Model):
    """Модель для збереження AI-аналітики (наприклад, прогнозів)."""
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="analyses")
    analysis_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.stock.symbol}"