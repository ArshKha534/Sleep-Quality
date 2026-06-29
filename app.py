from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return "Server is working! Next we will add the webpage."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
