import requests

domain = 'google.com'

file = open('./dictionaries/subdomains-1000.txt', 'r')

content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url = f'https://{subdomain}.{domain}'

    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print('Discovered Subdomain: ', url)