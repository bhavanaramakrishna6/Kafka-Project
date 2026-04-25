from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

counts = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.get_json()
    user = data.get('user')

    if user not in counts:
        counts[user] = 0

    counts[user] += 1

    print("Current Counts:", counts)

    return {"status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
