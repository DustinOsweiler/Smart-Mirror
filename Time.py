import http.client

conn = http.client.HTTPSConnection("world-clock.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "world-clock.p.rapidapi.com",
    'x-rapidapi-key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/json/cst/now", headers=headers)

res = conn.getresponse()
data = res.read()

time = (data.decode("utf-8"))
print(time)