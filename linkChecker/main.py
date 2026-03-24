import sys
import requests

try:
    with open("links.txt", 'r') as f:
        links = [line.strip() for line in f]

        for link in links:
            r = requests.get(link)

            if r.status_code == 200:
                print(f"{link} \t Opened \t Status Code: {r.status_code}")
            else:
                print(f"{link} \t Not Opened \t Status Code: {r.status_code}")
except FileNotFoundError:
    print("No links found")
except PermissionError:
    print("Permission denied")
