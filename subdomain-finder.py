import requests
import sys
from pyfiglet import Figlet
import threading

def search_subdomains(subs_chunk):
    for sub in subs_chunk:
        sub_domain = f"http://{sub}.{domain_name}"

        try:
            requests.get(sub_domain)
        except requests.ConnectionError:
            pass
        else:
            print(sub_domain)

def search(domain_name: str):
    f = Figlet(font="small")
    header = f.renderText("subdomain-finder")
    print(header)

    subdomains_list = open("subdomains-list.txt").read()
    subs = subdomains_list.splitlines()
    
    threads_num = 600
    subs_chunks = [subs[i:i + len(subs) // threads_num] for i in range(0, len(subs), len(subs) // threads_num)]
    threads = []
    for sub_chunk in subs_chunks:
        t = threading.Thread(target=search_subdomains, args=(sub_chunk,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    domain_name = sys.argv[1]
    search(domain_name)
