# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class APILog(models.Model):
#     """Логування API-запитів, щоб відстежувати використання OpenAI."""
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     request_data = models.TextField()
#     response_data = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"API Log {self.id} - {self.timestamp}"
