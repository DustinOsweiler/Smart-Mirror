import http.client

conn = http.client.HTTPSConnection("world-clock.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "world-clock.p.rapidapi.com",
    'x-rapidapi-key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/json/cst/now", headers=headers)

res = conn.getresponse()
data = res.read()

unprocessedtime = (data.decode("utf-8")).split(",")
timeanddate = unprocessedtime[1]
timeanddate = timeanddate.split("\"")
timeanddate = timeanddate[3]
timeanddate = timeanddate.split("T")
#print(timeanddate)

time = timeanddate[1]
time = time.split("-")
time = time[0]

date = timeanddate[0]

print(time)
print(date)