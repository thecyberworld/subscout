import requests
from pyfiglet import Figlet
from concurrent.futures import ThreadPoolExecutor
import argparse


def search_subdomain(sub):
    """Check if the subdomain is active and print it if it is."""
    sub_domain = f"http://{sub}.{domain_name}"

    try:
        response = requests.get(sub_domain, timeout=5)
        if response.status_code == 200:
            print(sub_domain)
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        print(f"Timeout while trying to access {sub_domain}")
    except requests.RequestException as e:
        print(f"Error occurred: {e}")


def search(domain_name: str):
    """Main function to read subdomains and initiate searching."""
    f = Figlet(font="small")
    header = f.renderText("SubScout")
    print(header)

    # Read subdomains from the file
    with open("subdomains-wordlist.txt", "r") as file:
        subs = file.read().splitlines()

    # Use ThreadPoolExecutor for efficient thread management
    max_workers = 100  # Adjust the number of workers as needed
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(search_subdomain, subs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Finder")
    parser.add_argument("domain", help="Domain name to search subdomains for")
    args = parser.parse_args()
    domain_name = args.domain
    search(domain_name)
