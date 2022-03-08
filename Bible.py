import http.client

conn = http.client.HTTPSConnection("bible-verse-of-the-day.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "bible-verse-of-the-day.p.rapidapi.com",
    'x-rapidapi-key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/", headers=headers)

res = conn.getresponse()
data = res.read()

#Bible = 
print(data.decode("utf-8"))
