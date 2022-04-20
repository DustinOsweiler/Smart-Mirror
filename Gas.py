import http.client

conn = http.client.HTTPSConnection("gas-price.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "gas-price.p.rapidapi.com",
    'x-rapidapi-key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/stateUsaPrice?state=WI", headers=headers)

res = conn.getresponse()
data = res.read()

gas = (data.decode("utf-8"))
print(gas)