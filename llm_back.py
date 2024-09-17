import os
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from flask import Flask, request, render_template, jsonify


llm_back = Flask(__name__)

#
def initialize_chatbot():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Provide response to the user queries"),
            ("user", "Question: {Question}")
        ]
    )
    
    llm = Ollama(model="llama3.1")
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    return chain

# Initialize chatbot
chain = initialize_chatbot()

@llm_back.route('/ai', methods=['POST'])
def back():
    request_data = request.get_json()
    output = chain.invoke({'Question': request_data.get('Question')})
    
    # Use following from Insomnia POST
    # output = chain.invoke({'Question': request_data['Question']})
   
    
    print(output)
    print("print at this point")
    
    # answer= {"Question": "Question",
    #          "answer":output}
    
    # print(answer["answer"])
    # return output
    # return answer["answer"]
    return jsonify({'result': output}), 200

      

# output, 200
# 3 values returned
# Need to check if the received expect 3 or 1 value

if __name__ == '__main__':
    llm_back.run(debug=True, port=5001)  # Run on port 5001




