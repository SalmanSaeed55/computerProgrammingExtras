"""
Link Checker Program

This program reads URLs from a file named 'links.txt' and checks their accessibility
by sending HTTP GET requests. It displays the results in a table format.
"""

import sys
import requests
from tabulate import tabulate

status_map = {
    200: "Accessible",
    404: "Not Found",
    403: "Access Forbidden",
    500: "Server Error",
    301: "Redirected",
    302: "Redirected",
}

try:
    with open("links.txt", "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip()]

        if not links:
            print("No links to check")
            sys.exit()

        results = []
        for link in links:
            try:
                response = requests.get(link, timeout=5)

                # pylint: disable=invalid-name
                status_code = str(response.status_code)
                status_text = status_map.get(
                    response.status_code, f"Error (Status Code: {response.status_code})"
                )
            except requests.exceptions.RequestException:
                # pylint: disable=invalid-name
                status_text = "Network Error"
                status_code = "N/A"

            results.append([link, status_text, status_code])

        print(
            tabulate(
                results,
                headers=["URL", "Status", "Code"],
                tablefmt="fancy_grid",
                maxcolwidths=[None, 50, None],
            )
        )
except FileNotFoundError:
    print("No links found")
except PermissionError:
    print("Permission denied")
