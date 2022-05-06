import http.client
import json

conn = http.client.HTTPSConnection("bible-search.p.rapidapi.com")

headers = {
    'X-RapidAPI-Host': "bible-search.p.rapidapi.com",
    'X-RapidAPI-Key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
    }

conn.request("GET", "/random-verse", headers=headers)

res = conn.getresponse()
data = res.read()

unprocessedBible = (data.decode("utf-8"))
unprocessedBible = json.loads(unprocessedBible)[0]
chapter = unprocessedBible['chapter']
verse = unprocessedBible['verse']
text = unprocessedBible['text']
book = unprocessedBible['book_name']

VerseOfDay = book + " " + str(chapter) + ":" + str(verse)
text =  "\"" + text + "\""

def getVerse():
    conn = http.client.HTTPSConnection("bible-search.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "bible-search.p.rapidapi.com",
        'X-RapidAPI-Key': "0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
        }

    conn.request("GET", "/random-verse", headers=headers)

    res = conn.getresponse()
    data = res.read()

    unprocessedBible = (data.decode("utf-8"))
    unprocessedBible = json.loads(unprocessedBible)[0]
    chapter = unprocessedBible['chapter']
    verse = unprocessedBible['verse']
    text = unprocessedBible['text']
    book = unprocessedBible['book_name']

    VerseOfDay = book + " " + str(chapter) + ":" + str(verse)
    text =  "\"" + text + "\""
    return(VerseOfDay, text)
#print(VerseOfDay)