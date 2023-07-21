import urllib.request
from bs4 import BeautifulSoup
import re
import os

# URL of the directory containing the files
base_url = 'https://publicdata.caida.org/datasets/topology/ark/ipv4/as-links/team-1/'

# Function to download a file given its URL
def download_file(file_url, directory):
    file_name = file_url.split('/')[-1]
    save_path = os.path.join(directory, file_name)
    urllib.request.urlretrieve(file_url, save_path)
    print(f"Downloaded: {save_path}")

# Function to recursively visit subdirectories
def visit_subdirectories(url, directory):
    # Fetch the HTML content of the URL
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all links ending with .txt.gz
    links = soup.find_all(href=re.compile(r'\.txt\.gz$'))

    # Download each file
    for link in links:
        file_url = url + link['href']
        download_file(file_url, directory)

    # Find all links pointing to subdirectories
    subdirectories = soup.find_all(href=re.compile(r'/$'))

    # Visit each subdirectory recursively
    for subdir in subdirectories:
        subdir_url = url + subdir['href']
        subdir_name = subdir['href'].strip('/')
        subdir_path = os.path.join(directory, subdir_name)
        os.makedirs(subdir_path, exist_ok=True)
        visit_subdirectories(subdir_url, subdir_path)

# Start visiting the base directory
visit_subdirectories(base_url, '.')
