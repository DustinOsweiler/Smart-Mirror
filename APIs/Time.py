import http.client
import json

conn = http.client.HTTPSConnection("world-clock.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "world-clock.p.rapidapi.com",
    'x-rapidapi-key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/json/cst/now", headers=headers)

res = conn.getresponse()
data = res.read()

unprocessedtime = (data.decode("utf-8"))
unprocessedtime = json.loads(unprocessedtime)
DateandTime = unprocessedtime['currentDateTime']
date = str(DateandTime).split("T")[0]

time = str(DateandTime).split("T")[1]
time = time.split("-")[0]
hour = time.split(":")[0]
hour = int(hour)

#print(hour)

pm = False
if hour > 12:
    hour = hour - 12
    pm = True

minutes = time.split(":")[1]

if pm == False:
    time = str(hour) + ":" + str(minutes) + " AM"
else:
    time = str(hour) + ":" + str(minutes) + " PM"

#print(unprocessedtime)
#print(time)
#print(date)