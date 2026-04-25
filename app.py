from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage (for deployment version)
counts = {}

# ------------------ ROUTES ------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


# ------------------ CLICK TRACKING ------------------

@app.route('/click', methods=['POST'])
def click():
    data = request.get_json()
    user = data.get('user')

    if user not in counts:
        counts[user] = 0

    counts[user] += 1

    print("Current Counts:", counts)

    return {"status": "success"}


# ------------------ RUN APP ------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
