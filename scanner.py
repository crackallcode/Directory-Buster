import requests
import argparse
import sys
from urllib.parse import urlparse

def enum(url):
    if not urlparse(url).scheme:
        return "http://" + url
    return url

def brute(base_url, wordlist):
    base_url = enum(base_url)  # Fixed function name 
    if not base_url.endswith('/'):
        base_url += '/'

    for word in wordlist:
        url = base_url + word.strip()  # fixed typo
        try: 
            response = requests.get(url, timeout=1)

            if response.status_code == 200:
                print(f"found {url}")
            else:
                print(f"Not found {url} {response.status_code}")

        except requests.exceptions.Timeout:  # fixed typo
            print(f"Timeout with {url}")
        except requests.ConnectionError:  # fixed typo
            print(f"Failed Connection {url}")

parser = argparse.ArgumentParser()
parser.add_argument("base_url")  # Fixed typo: changed 'add_arguemnt' to 'add_argument'
args = parser.parse_args()

wordlist = [line for line in sys.stdin]  
brute(args.base_url, wordlist)  
