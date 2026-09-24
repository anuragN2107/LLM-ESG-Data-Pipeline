from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_esg_report(url):
    print(f"Starting browser to scrape: {url}")
    
    # Configure Chrome to run in the background (headless mode)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # Modern Selenium headless argument
    
    # Initialize the webdriver
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        
        # Wait up to 15 seconds for the body tag to render
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Extract the raw text from the page
        raw_text = driver.find_element(By.TAG_NAME, "body").text
        print("Successfully extracted text!")
        return raw_text
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
        
    finally:
        driver.quit() # Always close the virtual browser

# Test the function with a sample URL
if __name__ == "__main__":
    target_url = "https://example.com"
    extracted_content = scrape_esg_report(target_url)
    
    # Print the first 200 characters to verify it worked
    if extracted_content:
        print("-" * 50)
        print(extracted_content[:200])
        print("-" * 50)