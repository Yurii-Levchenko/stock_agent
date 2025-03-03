import openai
from django.conf import settings

# openai.api_key = settings.OPENAI_API_KEY

# def get_ai_response(messages):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # or "gpt-3.5-turbo"
#         messages=messages
#     )
#     return response['choices'][0]['message']['content']
