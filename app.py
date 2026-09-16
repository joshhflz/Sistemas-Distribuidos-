from flask import Flask, request, jsonify

app = Flask(__name__)

# Route that handles both GET and POST requests
@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        # 1. Handle GET request
        # Retrieve query parameters from the URL (e.g., /api/data?name=Alice)
        user_name = request.args.get('name', 'Guest')
        
        return jsonify({
            "message": "GET request received successfully!",
            "greet": f"Hello, {user_name}!"
        }), 200

    elif request.method == 'POST':
        # 2. Handle POST request
        # Check if the client sent JSON data
        if request.is_json:
            data = request.get_json()
            item = data.get('item', 'unknown item')
            quantity = data.get('quantity', 0)
            
            return jsonify({
                "message": "POST JSON data received!",
                "received": {"item": item, "quantity": quantity}
            }), 201
            
        # Check if the client sent traditional HTML Form data
        elif request.form:
            form_item = request.form.get('item')
            return jsonify({
                "message": "POST Form data received!",
                "received_item": form_item
            }), 201
            
        else:
            return jsonify({"error": "Unsupported Media Type or empty body"}), 400

if __name__ == '__main__':
    # Run the local development server
    app.run(debug=True, port=5000)
