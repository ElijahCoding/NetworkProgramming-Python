import requests

domain = 'google.com'

file = open('./dictionaries/subdomains-1000.txt', 'r')

content = file.read()

subdomains = content.splitlines()

print(subdomains)