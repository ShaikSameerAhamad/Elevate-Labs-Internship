import requests
import json

BASE_URL = 'http://localhost:5000'

def test_api():
    print("Testing Flask REST API")
    print("=" * 40)
    
    # Test health check
    print("1. Health Check:")
    response = requests.get(f'{BASE_URL}/health')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test GET all users (empty)
    print("2. Get all users (should be empty):")
    response = requests.get(f'{BASE_URL}/users')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test POST - Create user
    print("3. Create new user:")
    user_data = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    response = requests.post(f'{BASE_URL}/users', json=user_data)
    print(f"Status: {response.status_code}")
    created_user = response.json()
    print(f"Response: {created_user}")
    user_id = created_user['id']
    print()
    
    # Test POST - Create another user
    print("4. Create second user:")
    user_data2 = {
        "name": "Jane Smith",
        "email": "jane@example.com"
    }
    response = requests.post(f'{BASE_URL}/users', json=user_data2)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test GET all users
    print("5. Get all users:")
    response = requests.get(f'{BASE_URL}/users')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test GET specific user
    print(f"6. Get user with ID {user_id}:")
    response = requests.get(f'{BASE_URL}/users/{user_id}')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test PUT - Update user
    print(f"7. Update user {user_id}:")
    update_data = {
        "name": "John Updated",
        "email": "john.updated@example.com"
    }
    response = requests.put(f'{BASE_URL}/users/{user_id}', json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test DELETE user
    print(f"8. Delete user {user_id}:")
    response = requests.delete(f'{BASE_URL}/users/{user_id}')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test GET all users after deletion
    print("9. Get all users after deletion:")
    response = requests.get(f'{BASE_URL}/users')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

if __name__ == '__main__':
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the Flask app is running on localhost:5000")
    except Exception as e:
        print(f"Error: {e}")