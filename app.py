from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for users
users = {}
next_id = 1

# Root route - API status
@app.route('/', methods=['GET'])
def api_status():
    user_count = len(users)
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask REST API</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; text-align: center; }}
            .status {{ text-align: center; font-size: 24px; color: #27ae60; margin: 20px 0; }}
            .endpoints {{ background: #ecf0f1; padding: 20px; border-radius: 5px; margin: 20px 0; }}
            .endpoint {{ margin: 10px 0; padding: 8px; background: white; border-left: 4px solid #3498db; }}
            .method {{ font-weight: bold; color: #e74c3c; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Flask REST API</h1>
            <div class="status">✅ API is running!</div>
            
            <div class="endpoints">
                <h3>Available Endpoints:</h3>
                <div class="endpoint"><span class="method">GET</span> / - API status page</div>
                <div class="endpoint"><span class="method">GET</span> /health - Health check</div>
                <div class="endpoint"><span class="method">GET</span> /users - Get all users</div>
                <div class="endpoint"><span class="method">GET</span> /users/&lt;id&gt; - Get specific user</div>
                <div class="endpoint"><span class="method">POST</span> /users - Create new user</div>
                <div class="endpoint"><span class="method">PUT</span> /users/&lt;id&gt; - Update user</div>
                <div class="endpoint"><span class="method">DELETE</span> /users/&lt;id&gt; - Delete user</div>
            </div>
            
            <p style="text-align: center; color: #7f8c8d;">
                Current users in database: <strong>{user_count}</strong>
            </p>
        </div>
    </body>
    </html>
    '''

# Helper function to validate user data
def validate_user_data(data):
    required_fields = ['name', 'email']
    if not data:
        return False, "No data provided"
    
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Missing or empty field: {field}"
    
    return True, None

# GET /users - Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        'users': list(users.values()),
        'count': len(users)
    })

# GET /users/<id> - Get specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(users[user_id])

# POST /users - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    
    data = request.get_json()
    is_valid, error_msg = validate_user_data(data)
    
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    # Check if email already exists
    for user in users.values():
        if user['email'] == data['email']:
            return jsonify({'error': 'Email already exists'}), 409
    
    user = {
        'id': next_id,
        'name': data['name'].strip(),
        'email': data['email'].strip(),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    users[next_id] = user
    next_id += 1
    
    return jsonify(user), 201

# PUT /users/<id> - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    is_valid, error_msg = validate_user_data(data)
    
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    # Check if email already exists for another user
    for uid, user in users.items():
        if uid != user_id and user['email'] == data['email']:
            return jsonify({'error': 'Email already exists'}), 409
    
    # Update user data
    users[user_id]['name'] = data['name'].strip()
    users[user_id]['email'] = data['email'].strip()
    users[user_id]['updated_at'] = datetime.now().isoformat()
    
    return jsonify(users[user_id])

# DELETE /users/<id> - Delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    deleted_user = users.pop(user_id)
    return jsonify({
        'message': 'User deleted successfully',
        'deleted_user': deleted_user
    })

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'users_count': len(users)
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)