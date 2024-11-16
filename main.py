import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
driver_path = r'C:\WebDriver\chromedriver.exe'

options = Options()
options.binary_location = brave_path
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-images")

def generate_views(url, views, delay):
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    print(f"Generating {views} views on {url} with a delay of {delay} seconds.")

    for i in range(1, views + 1):
        try:
            driver.get(url)
            print(f"View {i} generated successfully on {url}.")
            time.sleep(delay)
        except Exception as e:
            print(f"Error generating view {i}: {e}")
    
    driver.quit()

def main():
    try:
        print("Welcome to the Rapid View Bot with Selenium!")

        url_end = input("Enter the part of the URL after https://discord.me/ : ").strip()
        url = f"https://discord.me/{url_end}"

        if not url.startswith("https://discord.me/"):
            print("Error: The URL must start with https://discord.me/")
            return

        try:
            views = int(input("How many views would you like to generate? "))
            if views <= 0:
                print("Error: The number of views must be greater than 0.")
                return
        except ValueError:
            print("Error: You must enter a valid number.")
            return

        try:
            delay = float(input("Time between each view in seconds (min: 0.1) : "))
            if delay < 0.1:
                print("Error: The delay between each view must be at least 0.1 seconds.")
                return
        except ValueError:
            print("Error: You must enter a valid number for the delay.")
            return

        generate_views(url, views, delay)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
