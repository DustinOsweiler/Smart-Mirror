import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

conn.request("GET", "/v3/fixtures?season=2021&team=33", headers=headers)

res = conn.getresponse()
data = res.read()

soccer = (data.decode("utf-8"))
print(soccer)
