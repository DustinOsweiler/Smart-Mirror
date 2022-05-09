import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53140"}

headers = {
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
	"X-RapidAPI-Key": "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
}

response = requests.request("GET", url, headers=headers, params=querystring)

unprocessedweather = (response.text)
unprocessedweather = json.loads(unprocessedweather)
Location = unprocessedweather['location']
Location = Location['name']

#print(unprocessedweather)

unprocessedTemp = unprocessedweather['current']
Temp = unprocessedTemp['temp_f']

#print(unprocessedTemp)
#print(len(unprocessedTemp))

weatherURL = unprocessedTemp['condition']
weatherURL = weatherURL['icon']

def getTemp():
	url = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q":"53140"}

	headers = {
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
		"X-RapidAPI-Key": "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	unprocessedweather = (response.text)
	unprocessedweather = json.loads(unprocessedweather)
	Location = unprocessedweather['location']
	Location = Location['name']

	unprocessedTemp = unprocessedweather['current']
	Temp = unprocessedTemp['temp_f']

	weatherURL = unprocessedTemp['condition']
	weatherURL = weatherURL['icon']

	return(Temp)

def getLocation():
	url = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q":"53140"}

	headers = {
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
		"X-RapidAPI-Key": "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	unprocessedweather = (response.text)
	unprocessedweather = json.loads(unprocessedweather)
	Location = unprocessedweather['location']
	Location = Location['name']

	unprocessedTemp = unprocessedweather['current']
	Temp = unprocessedTemp['temp_f']

	weatherURL = unprocessedTemp['condition']
	weatherURL = weatherURL['icon']

	return(Location)

def getURL():
	url = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q":"53140"}

	headers = {
		"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
		"X-RapidAPI-Key": "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	unprocessedweather = (response.text)
	unprocessedweather = json.loads(unprocessedweather)
	Location = unprocessedweather['location']
	Location = Location['name']

	unprocessedTemp = unprocessedweather['current']
	Temp = unprocessedTemp['temp_f']

	weatherURL = unprocessedTemp['condition']
	weatherURL = weatherURL['icon']

	return(weatherURL)
	#print(Temp)