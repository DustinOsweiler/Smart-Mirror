import http.client

conn = http.client.HTTPSConnection("iq-bible.p.rapidapi.com")

headers = {
    'X-RapidAPI-Host': "iq-bible.p.rapidapi.com",
    'X-RapidAPI-Key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/GetRandomVerse?versionId=kjv", headers=headers)

res = conn.getresponse()
data = res.read()

Bible = (data.decode("utf-8"))
print(Bible)