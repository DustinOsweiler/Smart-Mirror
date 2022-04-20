import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53140"}

headers = {
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
	"X-RapidAPI-Key": "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
}

response = requests.request("GET", url, headers=headers, params=querystring)

weather = (response.text)
print(weather)