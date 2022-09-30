import requests
import sys
from pyfiglet import Figlet

f = Figlet(font='small')
print(f.renderText("subdomain-finder"))

subdomains_list = open("subdomains-list.txt").read()
subs = subdomains_list.splitlines()

for sub in subs:
    sub_domain = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domain)
    except requests.ConnectionError:
        pass
    else:
        print(sub_domain)
