import json
import urllib.request
filename = input("Δώσε όνομα αρχείου: ")
f = open(filename, "r")
dict = json.loads(f.read())
f.close()
a = len(dict)
value = list(dict.values())
crypto = list(dict.keys())
for i in range (a):
    str = crypto[i]
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + str + "&tsyms=EUR"
    r = urllib.request.urlopen(url)
    page_content = r.read()
    page_content = page_content.decode()
    dict2 = json.loads(page_content)
    output = str + " σε euro:"
    amount = dict2[str]["EUR"] * value[i]
    print("\n", output, amount)