# News Headlines Web Scraper

A Python script that scrapes news headlines from BBC News and Reuters, saving them to text files.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

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
