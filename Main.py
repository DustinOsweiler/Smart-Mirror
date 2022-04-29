from flask import Flask, render_template, jsonify, request
import APIs.Time as Time
import APIs.Bible as Bible
#import APIs.Gas as Gas
import APIs.Soccer as Soccer
import APIs.Weather as Weather
import APIs.Train as Train
#import APIs.News as News

app = Flask(__name__) #creating the Flask class object   

#@app.route("/time")
#def gettime():
time = Time.time
    #return jsonify(time)

#@app.route("/date")
#def getdate():
date = Time.date
    #jsonify(date)

#@app.route("/verse")
#def getverse():
verse = (Bible.VerseOfDay)
text = (Bible.text)
    #jsonify(verse)

#@app.route("/gas")
#def getgas():
    #gasprice = Gas.gas
    #jsonify(gasprice)

#@app.route("/soccer")
#def getsoccer():
homeScore = Soccer.homeScore
homeUrl = Soccer.homeLogo
awayScore = Soccer.awayScore
awayUrl = Soccer.awayLogo
    #jsonify(soccerstats)

#@app.route("/weather")
#def getweather():
weatherLoc = Weather.Location
weatherTemp = Weather.Temp
weatherUrl = Weather.weatherURL
    #jsonify(weather)

station = Train.Station
minutes = Train.Minutes

#Headline = News.Headline



 
@app.route('/') #decorator defines the   
def index():  
    return render_template('index.html', weatherLoc = weatherLoc, weatherURL = weatherUrl, weatherTemp = weatherTemp, 
    time = time, date = date, verse = verse, text = text, station = station, minutes = minutes, homeScore = homeScore, 
    awayScore = awayScore, homeUrl = homeUrl, awayUrl = awayUrl)  
  
if __name__ =='__main__':  
    app.run(debug = True)  