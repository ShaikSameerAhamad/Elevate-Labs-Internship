import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import sys
import os

class NewsHeadlinesScraper:
    def __init__(self):
        self.session = requests.Session()
        # Set a user agent to avoid being blocked
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.headlines = []
    
    def scrape_bbc_news(self):
        """Scrape headlines from BBC News"""
        try:
            print("Scraping BBC News headlines...")
            url = "https://www.bbc.com/news"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # BBC uses various selectors for headlines
            headline_selectors = [
                'h2[data-testid="card-headline"]',
                'h3[data-testid="card-headline"]',
                'h2.sc-4fedabc7-3',
                'h3.sc-4fedabc7-3',
                '.media__title a',
                '.gs-c-promo-heading__title'
            ]
            
            headlines_found = []
            for selector in headline_selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline = element.get_text(strip=True)
                    if headline and len(headline) > 10:  # Filter out very short text
                        headlines_found.append(headline)
            
            # Remove duplicates while preserving order
            seen = set()
            for headline in headlines_found:
                if headline not in seen:
                    self.headlines.append(f"[BBC] {headline}")
                    seen.add(headline)
            
            print(f"Found {len([h for h in self.headlines if h.startswith('[BBC]')])} BBC headlines")
            
        except requests.RequestException as e:
            print(f"Error scraping BBC News: {e}")
        except Exception as e:
            print(f"Unexpected error with BBC News: {e}")
    
    def scrape_reuters(self):
        """Scrape headlines from Reuters"""
        try:
            print("Scraping Reuters headlines...")
            url = "https://www.reuters.com"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Reuters headline selectors
            headline_selectors = [
                'h2[data-testid="Heading"]',
                'h3[data-testid="Heading"]',
                '.story-title',
                'h2 a[data-testid="Link"]',
                'h3 a[data-testid="Link"]'
            ]
            
            headlines_found = []
            for selector in headline_selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline = element.get_text(strip=True)
                    if headline and len(headline) > 10:
                        headlines_found.append(headline)
            
            # Remove duplicates
            seen = set()
            for headline in headlines_found:
                if headline not in seen:
                    self.headlines.append(f"[Reuters] {headline}")
                    seen.add(headline)
            
            print(f"Found {len([h for h in self.headlines if h.startswith('[Reuters]')])} Reuters headlines")
            
        except requests.RequestException as e:
            print(f"Error scraping Reuters: {e}")
        except Exception as e:
            print(f"Unexpected error with Reuters: {e}")
    
    def scrape_example_news_site(self):
        """Example method for scraping a generic news site"""
        try:
            print("Scraping example news site...")
            # Example URL - replace with actual news site
            url = "https://example-news-site.com"
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Common selectors for headlines
            headline_selectors = [
                'h1',
                'h2', 
                'h3',
                '.headline',
                '.title',
                '.article-title',
                '[class*="headline"]',
                '[class*="title"]'
            ]
            
            for selector in headline_selectors:
                elements = soup.select(selector)
                for element in elements:
                    headline = element.get_text(strip=True)
                    if headline and len(headline) > 10:
                        self.headlines.append(f"[Example] {headline}")
            
        except requests.RequestException as e:
            print(f"Error scraping example site: {e}")
    
    def scrape_all_sites(self):
        """Scrape headlines from all configured news sites"""
        print("Starting news headline scraping...")
        print("=" * 50)
        
        # Add delay between requests to be respectful
        self.scrape_bbc_news()
        time.sleep(2)  # 2-second delay
        
        self.scrape_reuters()
        time.sleep(2)
        
        # Uncomment to add more sites
        # self.scrape_example_news_site()
        
        print("=" * 50)
        print(f"Total headlines scraped: {len(self.headlines)}")
    
    def save_headlines_to_file(self, filename="news_headlines.txt"):
        """Save scraped headlines to a text file"""
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
            
            with open(filename, 'w', encoding='utf-8') as f:
                # Write header
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"News Headlines Scraped on: {timestamp}\n")
                f.write("=" * 60 + "\n\n")
                
                # Write headlines
                for i, headline in enumerate(self.headlines, 1):
                    f.write(f"{i:3d}. {headline}\n")
                
                # Write footer
                f.write(f"\n" + "=" * 60 + "\n")
                f.write(f"Total headlines: {len(self.headlines)}\n")
            
            print(f"Headlines saved to: {filename}")
            return True
            
        except Exception as e:
            print(f"Error saving headlines to file: {e}")
            return False
    
    def display_headlines(self, max_display=10):
        """Display headlines in the console"""
        if not self.headlines:
            print("No headlines found.")
            return
        
        print("\nLatest Headlines Preview:")
        print("-" * 40)
        
        for i, headline in enumerate(self.headlines[:max_display], 1):
            print(f"{i:2d}. {headline}")
        
        if len(self.headlines) > max_display:
            print(f"    ... and {len(self.headlines) - max_display} more headlines")

def main():
    """Main function to run the news scraper"""
    scraper = NewsHeadlinesScraper()
    
    try:
        # Scrape headlines from all sites
        scraper.scrape_all_sites()
        
        if scraper.headlines:
            # Display a preview
            scraper.display_headlines()
            
            # Save to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"news_headlines_{timestamp}.txt"
            
            if scraper.save_headlines_to_file(filename):
                print(f"\n✅ Success! Headlines saved to '{filename}'")
            else:
                print("\n❌ Failed to save headlines to file")
        else:
            print("\n⚠️  No headlines were scraped. Check your internet connection and try again.")
    
    except KeyboardInterrupt:
        print("\n\n⏹️  Scraping interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
