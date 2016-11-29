#! /usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests
import sys, os
import markdown
import html2text

# Get the URL from cli
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print ("Usage: python3 "+ os.path.basename(__file__) +" <URL>")
    quit()

# Get the main-content div from the page 
r = requests.get(url)
soup = bs(r.text, 'lxml')
d = soup.find("div", {"id": "main-content"})

# Blacklist the nav tag
blacklist=['nav']
for tag in d.findAll():
    if tag.name.lower() in blacklist:
        tag.extract()

# Extract content in markdown
for r in d.contents:
    if r:
        print (html2text.html2text(str(r)))
