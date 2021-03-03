from urllib import request
import urllib
from urllib.request import urlopen
import json
from datetime import date
from time import sleep
today = date.today()
url = "https://api.opap.gr/games/v1.0/51new03/statistics"
r = urllib.request.urlopen(url)
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
html = r.read()
html = html.decode()
data= json.loads(html, strict=False)
for draw in data["content"]:
    print(draw["WinningNumbers"])["list"] 