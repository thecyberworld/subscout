import requests
import sys
from pyfiglet import Figlet


def search(domain_name: str):
    f = Figlet(font="small")
    header = f.renderText("subdomain-finder")
    print(header)

    subdomains_list = open("subdomains-list.txt").read()
    subs = subdomains_list.splitlines()

    for sub in subs:
        sub_domain = f"http://{sub}.{domain_name}"

        try:
            requests.get(sub_domain)
        except requests.ConnectionError:
            pass
        else:
            print(sub_domain)


if __name__ == "__main__":
    domain_name = sys.argv[1]
    search(domain_name)
