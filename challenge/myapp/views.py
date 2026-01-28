from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import google.generativeai as genai
from django.conf import settings
import json

genai.configure(api_key=settings.GOOGLE_API_KEY)
print("Gemini API Key:", settings.GOOGLE_API_KEY)
model = genai.GenerativeModel(
    "gemini-3-flash",
    system_instruction="You are a grammar checker. Check the user's input text and returna list of errors found in the text along with their corrections and the type of error.")
chat = model.start_chat(history=[])

@csrf_exempt
def input_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        response = chat.send_message(user_message)
        bot_reply = response.text
        return JsonResponse({"reply": bot_reply})
    return render(request, "chat.html")
