import http.client

conn = http.client.HTTPSConnection("bible-verse-of-the-day.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "bible-verse-of-the-day.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

conn.request("GET", "/", headers=headers)

res = conn.getresponse()
data = res.read()

#Bible = 
print(data.decode("utf-8"))
