import urllib.request, json

# Opening a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=n&apiKey=ba85672fd88fbdcf2a48")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
results = data['results']
ILS_USD = results['ILS_USD']
val = ILS_USD['val']
ILS = input("Welcome to currency converter \nPlease enter an amount of Shekeles to convert:")
print(int(ILS) * val)
print("Thanks for using our currency converter!")