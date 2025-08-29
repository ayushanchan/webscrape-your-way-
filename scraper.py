import requests
from bs4 import BeautifulSoup
import sys

def get_website_title(url):
    """
    Our robot reporter function
    - Takes a website URL
    - Visits the website
    - Finds and returns the title
    """
    try:
        print(f"🤖 Reporter visiting: {url}")
        
        # Send our robot to the website
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if request was successful
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the title tag
        title_tag = soup.find('title')
        
        if title_tag:
            title = title_tag.get_text().strip()
            print(f"📰 Found title: '{title}'")
            return title
        else:
            print("❌ No title found on this page")
            return "No title found"
            
    except requests.RequestException as e:
        print(f"❌ Error visiting website: {e}")
        return f"Error: {e}"

def main():
    """
    Main function - this runs when our reporter starts working
    """
    # Default website to visit (you can change this)
    default_url = "http://example.com"
    
    # Check if user provided a different URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = default_url
    
    print("🚀 Robot Reporter Starting...")
    print("=" * 40)
    
    # Send our reporter to work!
    title = get_website_title(url)
    
    print("=" * 40)
    print(f"📋 REPORT: The title of '{url}' is:")
    print(f"    '{title}'")
    print("✅ Reporter mission complete!")

if __name__ == "__main__":
    main()