
# Flask REST API - User Management

A simple REST API built with Flask for managing user data with full CRUD operations.

## Features

- **GET /users** - Retrieve all users
- **GET /users/<id>** - Retrieve a specific user
- **POST /users** - Create a new user
- **PUT /users/<id>** - Update an existing user
- **DELETE /users/<id>** - Delete a user
- **GET /health** - Health check endpoint
- **GET /** - API status page (HTML)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask app:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Quick Start

Visit `http://localhost:5000/` in your browser to see the API status page with all available endpoints.

## API Usage Examples

### Check API status (Browser)
Visit `http://localhost:5000/` - Shows a nice HTML page with "API is running!"

### Health check
```bash
curl http://localhost:5000/health
```

### Create a user
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Get all users
```bash
curl http://localhost:5000/users
```

### Get specific user
```bash
curl http://localhost:5000/users/1
```

### Update a user
```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Updated", "email": "john.updated@example.com"}'
```

### Delete a user
```bash
curl -X DELETE http://localhost:5000/users/1
```

## Testing

Run the automated test script:
```bash
python test_api.py
```

Make sure the Flask app is running before executing the tests.

## Data Structure

Users are stored with the following structure:
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-01T12:00:00",
  "updated_at": "2024-01-01T12:00:00"
}
```

