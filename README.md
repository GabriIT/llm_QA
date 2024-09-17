#The app is a simple Flask app that uses a pre-trained LLM (Llama 3.1) to generate answer based on user input. The app has a single route that accepts POST requests with a JSON payload containing a "prompt" field. 
The UI is UI_llm.py in env flask
The backend is llm_back.py in env gpu

The Flask router is at 5000 with a web interface to input a query.
It is not using Insomnia/Postman.

Using the App in folder "UI_flask_llm" the UI is a website.
