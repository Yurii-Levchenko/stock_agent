from django.shortcuts import render

# Creating a New Chat Session
# chat_session = ChatSession.objects.create(user=request.user)

# Adding a Message to a Session
# ChatMessage.objects.create(
#     session=chat_session,
#     sender=request.user,
#     message="What is the best stock to invest in?"
# )

# Retrieving a User’s Chat Sessions
# user_sessions = ChatSession.objects.filter(user=request.user)

# Getting Messages for a Specific Chat Session
# messages = ChatMessage.objects.filter(session=chat_session).order_by("timestamp")


# sender_name = message.session.user.username if message.sender == 'user' else 'AI'




# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import ChatSession, ChatMessage
# from .utils import get_ai_response

# class ChatAPIView(APIView):
#     def post(self, request):
#         user = request.user
#         session, created = ChatSession.objects.get_or_create(user=user)
        
#         user_message = request.data.get("message")
#         ChatMessage.objects.create(session=session, sender="user", message=user_message)

#         ai_response = get_ai_response([{"role": "user", "content": user_message}])
#         ChatMessage.objects.create(session=session, sender="ai", message=ai_response)

#         return Response({"response": ai_response})
