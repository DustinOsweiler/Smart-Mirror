import requests
import json

url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"

querystring = {"key": "06b16acbd57740e0be407db252b2928f", "stpid":"30295", "outputType": "JSON"}

response = requests.request("GET", url, params=querystring)

unprocessedTrain = (response.text)
Train = json.loads(unprocessedTrain)
MoreTrain = Train['ctatt']
EvenMoreTrain = MoreTrain['eta'][0]

Station = EvenMoreTrain["staNm"]
arrt = EvenMoreTrain["arrT"]
arrt = str(arrt)
arrt = arrt.split(":")[1]
prdt = EvenMoreTrain["prdt"]
prdt = str(prdt)
prdt = prdt.split(":")[1]

#print(arrt, prdt)
#print(unprocessedTrain)

if arrt < prdt:
    arrt = int(arrt) + 60

Minutes = int(arrt) - int(prdt)

#print(Station, Minutes)