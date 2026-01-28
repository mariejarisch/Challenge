from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import google.generativeai as genaiv
from django.conf import settings
import json

# configuration of Gemini API with GOOGLE_API_KEY, specifying the model and system instruction
genai.configure(api_key=settings.GOOGLE_API_KEY)
print("Gemini API Key:", settings.GOOGLE_API_KEY)
model = genai.GenerativeModel(
    "gemini-3.0-flash",
    system_instruction="You are a grammar checker. Check the user's input text and return a list of errors found in the text along with their corrections and the type of error.")
chat = model.start_chat(history=[])

@csrf_exempt
# input view where user input can happen
def input_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        # send message to chat/API and receive response
        response = chat.send_message(user_message)
        bot_reply = response.text
        return JsonResponse({"reply": bot_reply})
    return render(request, "chat.html")
