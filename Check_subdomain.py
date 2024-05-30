import requests
import time
from tabulate import tabulate


subdomains = [
    'https://www.netflix.com/in/',
    'https://www.netflix.com/login',
    'https://www.netflix.com/signup/registration?locale=en-IN',
]

def check_subdomain_status(subdomains):
    status_list = []
    for subdomain in subdomains:
        try:
            response = requests.get(subdomain, timeout=5)
            status = 'Up' if response.status_code == 200 else 'Down'
        except requests.RequestException:
            status = 'Down'
        status_list.append((subdomain, status))
    return status_list

def display_status_table(status_list):
    table = tabulate(status_list, headers=['Subdomain', 'Status'], tablefmt='grid')
    print(table)
  

def main():
    while True:
        status_list = check_subdomain_status(subdomains)
        display_status_table(status_list)
        print(status_list)
        time.sleep(60) 

if __name__ == "__main__":
    main()
