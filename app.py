from flask import Flask,request,jsonify
from chatbot import first

app=Flask(__name__)
bot = first("dataset.json")

@app.route('/', methods=['GET'])
def home():
    return "✅ Chatbot API is running. "

@app.route('/', methods=['POST'])
def chat():
    data = request.get_json()
    user = data.get('message', '')
    
    if not user:
        return jsonify({"error": "No message provided"}), 400

    response = bot.get_data(user)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run()