"""Steps:
- 1: Scrap player data from "https://www.pro-football-reference.com/ for specific season
- 2: Calculate fantasy points depending on rules
- 3: Find best draft strategy:
    a) Based on 'rules'
    b) Some kind of AI (This is for learning)"""

import urllib.request
import urllib.error
import sys
"""Get data from website"""
url = "https://www.pro-football-reference.com/years/"
year = 2020

"""Check if website is available"""
try:
    url_answer_code = urllib.request.urlopen(url+str(year)).getcode()
except urllib.error.URLError:
    print("Page not found")
    sys.exit(1)

print("test 2")

