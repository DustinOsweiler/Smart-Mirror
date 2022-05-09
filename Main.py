from flask import Flask, render_template, jsonify, request
import APIs.Time as Time
import APIs.Bible as Bible
#import APIs.Gas as Gas
import APIs.Soccer as Soccer
import APIs.Weather as Weather
import APIs.Train as Train
import APIs.News as News
import APIs.FitBit as fb
import APIs.Budget as Budget

app = Flask(__name__) #creating the Flask class object 

repeat = True

@app.route("/time", methods = ['POST'])
def gettime():
    nowtime = Time.getTime()
    #print(nowtime)
    return jsonify('', render_template('time.html', time = nowtime))

time = Time.getTime()
#Time.getDateandTime()

@app.route("/date", methods = ['POST'])
def getdate():
    nowdate = Time.getDate()
    return jsonify('', render_template('date.html', date = nowdate))

date = Time.getDate()

@app.route("/verse", methods = ['POST'])
def getverse():
    bible = Bible.getVerse()
    verse = bible[0]
    text = bible[1]
    return jsonify('', render_template('Bible.html', verse = verse, text = text))

verse = (Bible.VerseOfDay)
text = (Bible.text)

#@app.route("/gas", methods = ['POST'])
#def getgas():
    #jsonify(Gas.gas)

#gasprice = Gas.gas

@app.route("/soccer", methods = ['POST'])
def getsoccer():
    soccerstats = Soccer.getSoccer
    homeScore = soccerstats[1]
    homeUrl = soccerstats[0]
    awayScore = soccerstats[3]
    awayUrl = soccerstats[2]
    gameDate = soccerstats[4]
    return jsonify('', render_template('Soccer.html', homeScore = homeScore, homeUrl = homeUrl, awayScore = awayScore, awayUrl = awayUrl, gameDate = gameDate))

homeScore = Soccer.homeScore
homeUrl = Soccer.homeLogo
awayScore = Soccer.awayScore
awayUrl = Soccer.awayLogo
gameDate = Soccer.GameDate

@app.route("/weather", methods = ['POST'])
def getweather():
    weatherLocation = Weather.getLocation()
    weatherTemp = Weather.getTemp()
    weatherUrl = Weather.getURL()
    return jsonify('', render_template('weather.html', weatherLoc = weatherLocation, weatherTemp = weatherTemp, weatherURL = weatherUrl)) 

weatherLoc = Weather.Location
weatherTemp = Weather.Temp
weatherUrl = Weather.weatherURL

@app.route("/train", methods = ['POST'])
def gettrain():
    train = Train.getTrain()
    station = train[0]
    minutes = train[1]
    color = train[2]
    return jsonify('', render_template('Train.html', station = station, minutes = minutes, color = color))

station = Train.Station
minutes = Train.Minutes
color = Train.lineColor

@app.route("/news", methods = ['POST'])
def getnews():
    newNews = News.getNews()
    Headline = newNews[0]
    Favicon = newNews[1]
    return jsonify('', render_template('News.html', News = Headline, Favicon = Favicon))

Headline = News.Headline
Favicon = News.Favicon
#Headline = "News"

@app.route("/fitbit", methods = ['POST'])
def getfitbit():
    info = fb.getFitbit()
    stepGoal = info[1]
    name = info[2]
    dailySteps = info[3]
    activeMinutes = info[0]
    icon = info[4]
    return jsonify('', render_template('FitBit.html', stepGoal = stepGoal, dailySteps = dailySteps, name = name, activeGoal = activeMinutes, icon = icon))

stepGoal = fb.stepGoal
name = fb.Name
dailySteps = fb.dailySteps
activeMinutes = fb.activegoal
icon = fb.icon

@app.route("/budget", methods = ['POST'])
def getbudget():
    spent = Budget.getSpent()
    budget = Budget.getTotal()
    output = Budget.getOutput()
    left = Budget.getLeft()
    return jsonify('', render_template('Budget.html', spent = spent, budget = budget, output = output, left = left))

spent = Budget.TotalSpent
budget = Budget.TotalBudget
output = Budget.output
left = Budget.left

 
@app.route('/') #decorator defines the   
def index():  
    return render_template('index.html', weatherLoc = weatherLoc, weatherURL = weatherUrl, weatherTemp = weatherTemp, 
    time = time, date = date, verse = verse, text = text, station = station, minutes = minutes, homeScore = homeScore, 
    awayScore = awayScore, homeUrl = homeUrl, awayUrl = awayUrl, gameDate = gameDate, stepGoal = stepGoal, name = name, dailySteps = dailySteps,
    activeGoal = activeMinutes, icon = icon, spent = spent, budget = budget, output = output, left = left, News = Headline, color = color, Favicon = Favicon)  

if __name__ =='__main__':  
    app.run(debug = True)  
