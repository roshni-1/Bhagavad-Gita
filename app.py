from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace 'your-secret-key' with an actual secret key for security
SECRET_KEY = '1234'

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/webhook', methods=['POST'])
def webhook_handler():
    # Validate the webhook request (replace with your own validation logic)
    if request.headers.get('X-Hub-Signature') != f'sha1={SECRET_KEY}':
        return jsonify({"error": "Unauthorized"}), 401

    try:
        # Process the incoming payload
        data = request.json
        # Add your logic to handle the payload data

        # Respond to the webhook request
        return jsonify({"message": "Webhook received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
       
        import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)


if __name__ == '__main__':
    app.run(debug=True)
