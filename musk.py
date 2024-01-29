import requests
from bs4 import BeautifulSoup
import csv

# The URL of the website you want to scrape
url = 'https://httpbin.org/html'

# Headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send a GET request to the website
try:
    response = requests.get(url, headers=headers)
    # Raise an exception if the response status is an error
    response.raise_for_status()

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find elements by tag, this example finds all paragraph tags
    elements = soup.find_all('p')
    
    # Specify the absolute path for the CSV file
    file_path = 'C:\Project\scraped_data.csv'
    
    # Open a CSV file for writing
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Optional: write a header row
        writer.writerow(['Paragraph Text'])
        
        # Iterate through each element and write its text content to the CSV
        for element in elements:
            writer.writerow([element.text])

    print("Scraping completed and data saved to CSV.")

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'An error occurred: {err}')

