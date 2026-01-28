# Challenge
## How to run the code
(Normally, but I pushed everything:
1. Create a virtual environment by running python -m venv venv and activate it using venv\Scripts\activate.
2. Install dependencies with python -m pip install -r requirements.txt.)

1. Run python manage.py runserver to start the development server.
2. Input text that should be checked into the input field.

## Challenges
- expected frontend challenge, but then simply started this one
- as a student more used to “taking over”/joining existing projects, many of them not having a clear backend/frontend structure
- after user input no reply, was unfortunately not able to resolve this in the designated time period

## Design choices
- chose Django because it is a popular framework with a lot of built-in features, allows development of robust applications
- installed the Django REST framework because we are building an API
- chose Gemini because it is one of the most commonly used models, very capable for text processing and generation nowadays
-chose Gemini 3 Flash because it is the current most balanced Gemini model, prioritizes speed and scalability
- interaction with Gemini: model like interaction with a chatbot as a simplification because of time constraints, which is a matching metaphor for the required communication (user input->response); then further specify interaction with system_instruction for model
- therefore using HTML page accessible through development server to input text as of now


## Future improvements/additions
- remove “chatbot” structure, instead of textual reply return result as type list (including the list of errors found in the text along with their corrections and the type of error)
- test API with different input lengths, different grammatical errors
- evaluate response time, correctness
