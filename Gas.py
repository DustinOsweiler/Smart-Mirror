import http.client

conn = http.client.HTTPSConnection("gas-price.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "gas-price.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

conn.request("GET", "/stateUsaPrice?state=WI", headers=headers)

res = conn.getresponse()
data = res.read()

gas = (data.decode("utf-8"))
print(gas)
