<<<<<<< HEAD
# Flask REST API - User Management

A simple REST API built with Flask for managing user data with full CRUD operations.

## Features

- **GET /users** - Retrieve all users
- **GET /users/<id>** - Retrieve a specific user
- **POST /users** - Create a new user
- **PUT /users/<id>** - Update an existing user
- **DELETE /users/<id>** - Delete a user
- **GET /health** - Health check endpoint
=======
# News Headlines Web Scraper

A Python script that scrapes news headlines from BBC News and Reuters, saving them to text files.
>>>>>>> a0d887bd4c23c00a79039528dcdc133339595f2a

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
2. Run the Flask app:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Usage Examples

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
=======
2. Run the scraper:
```bash
python news_scraper.py
```

## Output

The script creates timestamped files like `news_headlines_20250807_143022.txt` containing:

```
News Headlines Scraped on: 2025-08-07 14:30:22

  1. [BBC] Global climate summit reaches breakthrough agreement  
  2. [Reuters] Central bank announces interest rate decision
  3. [BBC] Technology stocks surge amid AI investment boom
  
Total headlines: 25
```

## Adding New Sites

Create a new scraping method in the `NewsHeadlinesScraper` class:

```python
def scrape_new_site(self):
    url = "https://newssite.com"
    response = self.session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for element in soup.select('h2, h3'):  # Adjust selectors
        headline = element.get_text(strip=True)
        if headline:
            self.headlines.append(f"[NewSite] {headline}")
```

Add it to `scrape_all_sites()` method and include a 2-second delay.

## Dependencies

- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing  
- `lxml` - Parser backend

## Notes

- Includes 2-second delays between requests
- Removes duplicate headlines automatically
- Check website's robots.txt and terms of service before scraping
- Some sites may block automated requests
>>>>>>> a0d887bd4c23c00a79039528dcdc133339595f2a
