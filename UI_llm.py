# Calculator app
from flask import Flask, request, jsonify, render_template
import requests
import time

secret = "CLqR9gk4vR4wxtADim9PX8iJFhTFrN7i"


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the 'index.html' template


@app.route('/query', methods=['POST'])
def query():
    request_data = request.get_json()
    query = request_data.get('Question')
    print(request_data)
    print(query)


    # if not query:
    #     return jsonify({'error': 'Missing "query" parameter'}), 400

    result = send_to_back(request_data)
    
           
       
    response = f"Your query: '{query}'. {result} "
    print(response)

    return jsonify({'response': response})

def send_to_back(Question):
  url = f'http://localhost:5001/ai'  # URL of the 'Back' app
  response = requests.post(url, json={'Question': Question })

  if response.status_code == 200:
    print(response.status_code, response.text)
    
    return response.text
    
  else:
    raise Exception(f"Error sending to Back app: {response.status_code} - {response.text}")

if __name__ == '__main__':
    app.run(debug=True)
