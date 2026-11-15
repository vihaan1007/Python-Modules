import urllib.request, urllib.parse 

response = urllib.request.urlopen("https://example.com")
data = response.read()

print(data)

params = {
    "Name": "A",
    "Age": 9
}

query= urllib.parse.urlencode(params)
print(query)

import urllib.error

try:
    urllib.request.urlopen("https://wrong-url-example.com")
except urllib.error.URLError as e:
    print("Error:", e)
