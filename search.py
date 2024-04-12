#Author: Reza Rafati 
#Date: 12-04-2024
#Description: Quickly grab content from Google for further investigation.
#python3 search.py
#-------------------------------------------
from googlesearch import search
import os
import requests
from urllib.parse import urlparse
from pathlib import Path
import time

def download_pdf(title, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if 'application/pdf' in content_type:
                url_parsed = urlparse(url)
                domain = url_parsed.netloc
                pdf_name = url_parsed.path.split('/')[-1]

                # Create directory if it doesn't exist
                storage_path = os.path.join('storage', domain)
                Path(storage_path).mkdir(parents=True, exist_ok=True)

                # Save PDF file
                with open(os.path.join(storage_path, pdf_name), 'wb') as f:
                    f.write(response.content)
                    print(f"Downloaded {pdf_name} from {domain}")
        else:
            print(f"Failed to fetch PDF from {url}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

def google_search(query):
    try:
        search_results = search(query,num_results=100,advanced=True) # You can adjust the parameters as needed
        for i in search_results: 
            download_pdf(i.title,i.url)
            time.sleep(2)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    query = "site:threatintelligencelab.com filetype:pdf"
    google_search(query)
