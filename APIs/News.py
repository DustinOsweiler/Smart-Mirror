import http.client
import json

conn = http.client.HTTPSConnection("google-news1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Host': "google-news1.p.rapidapi.com",
    'X-RapidAPI-Key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/top-headlines?country=US&lang=en&limit=50", headers=headers)

res = conn.getresponse()
data = res.read()

unprocessedNews = (data.decode("utf-8"))
unprocessedNews = json.loads(unprocessedNews)
#print(unprocessedNews)
topHeadline = (unprocessedNews['articles'])[0]
#print(topHeadline)
Headline = topHeadline['title']

def getNews():
    conn = http.client.HTTPSConnection("google-news1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "google-news1.p.rapidapi.com",
        'X-RapidAPI-Key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
        }

    conn.request("GET", "/top-headlines?country=US&lang=en&limit=50", headers=headers)

    res = conn.getresponse()
    data = res.read()

    unprocessedNews = (data.decode("utf-8"))
    unprocessedNews = json.loads(unprocessedNews)
    topHeadline = (unprocessedNews['articles'])[0]
    Headline = topHeadline['title']

    #print(Headline)
    
    return(Headline)