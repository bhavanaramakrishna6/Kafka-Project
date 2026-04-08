from flask import Flask, request, render_template
from flask_cors import CORS
from kafka import KafkaProducer
import json

app = Flask(__name__)
CORS(app)

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.get_json()

    user = data.get('user')
    button = data.get('page')

    event = {
        "user": user,
        "button": button
    }

    producer.send('clicks', value=event)
    producer.flush()

    return {"status": "success"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
