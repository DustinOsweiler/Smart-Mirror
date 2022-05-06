from statistics import linear_regression
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
#print(EvenMoreTrain)
lineColor = EvenMoreTrain['rt']
if lineColor == "G":
    lineColor = "Green"
lineColor = lineColor.lower()

#print(lineColor)


if arrt < prdt:
    arrt = int(arrt) + 60

timeUntil = int(arrt) - int(prdt)

Minutes = str(int(arrt) - int(prdt)) + " Minutes"

if timeUntil <= 1:
        Minutes = "Arriving" 

#print(Minutes, Station)


def getTrain():
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

    lineColor = EvenMoreTrain['rt']
    if lineColor == "G":
        lineColor = "Green"
    lineColor = lineColor.lower()

    if arrt < prdt:
        arrt = int(arrt) + 60

    timeUntil = int(arrt) - int(prdt)

    Minutes = str(int(arrt) - int(prdt)) + " Minutes"

    if timeUntil <= 1:
        Minutes = "Arriving" 

    return(Station, Minutes, lineColor)

    #print(Station, Minutes)