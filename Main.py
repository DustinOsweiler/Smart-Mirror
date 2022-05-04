from flask import Flask, render_template, jsonify, request
import APIs.Time as Time
import APIs.Bible as Bible
#import APIs.Gas as Gas
import APIs.Soccer as Soccer
import APIs.Weather as Weather
import APIs.Train as Train
#import APIs.News as News
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
    #jsonify(Bible.VerseOfDay, Bible.text)
    verse = (Bible.VerseOfDay)
    text = (Bible.text)

verse = (Bible.VerseOfDay)
text = (Bible.text)

#@app.route("/gas", methods = ['POST'])
#def getgas():
    #jsonify(Gas.gas)

#gasprice = Gas.gas

@app.route("/soccer", methods = ['POST'])
def getsoccer():
    #jsonify(Soccer.GameDate, Soccer.awayLogo, Soccer.awayScore, Soccer.homeLogo, Soccer.homeScore)
    homeScore = Soccer.homeScore
    homeUrl = Soccer.homeLogo
    awayScore = Soccer.awayScore
    awayUrl = Soccer.awayLogo
    gameDate = Soccer.GameDate

homeScore = Soccer.homeScore
homeUrl = Soccer.homeLogo
awayScore = Soccer.awayScore
awayUrl = Soccer.awayLogo
gameDate = Soccer.GameDate

@app.route("/weather", methods = ['POST'])
def getweather():
    weatherLocation = Weather.getLocation()
    weatherTemp = Weather.getTemp
    weatherUrl = Weather.getURL
    return jsonify('', render_template('weather.html', weatherLoc = weatherLocation, weatherTemp = weatherTemp, weatherURL = weatherUrl)) 

weatherLoc = Weather.Location
weatherTemp = Weather.Temp
weatherUrl = Weather.weatherURL

@app.route("/train", methods = ['POST'])
def gettrain():
    jsonify(Train.Station, Train.Minutes)
    station = Train.Station
    minutes = Train.Minutes

station = Train.Station
minutes = Train.Minutes

#@app.route("/news", methods = ['POST'])
#def getnews():
#    jsonify(News.Headline)

#Headline = News.Headline

@app.route("/fitbit", methods = ['POST'])
def getfitbit():
    #jsonify(fb.stepGoal, fb.Name, fb.dailySteps, fb.activegoal, fb.icon)
    stepGoal = fb.stepGoal
    name = fb.Name
    dailySteps = fb.dailySteps
    activeMinutes = fb.activegoal
    icon = fb.icon

stepGoal = fb.stepGoal
name = fb.Name
dailySteps = fb.dailySteps
activeMinutes = fb.activegoal
icon = fb.icon

@app.route("/budget", methods = ['POST'])
def getbudget():
    #jsonify(Budget.TotalSpent, Budget.TotalBudget, Budget.output, Budget.left)
    spent = Budget.TotalSpent
    budget = Budget.TotalBudget
    output = Budget.output
    left = Budget.left

spent = Budget.TotalSpent
budget = Budget.TotalBudget
output = Budget.output
left = Budget.left

 
@app.route('/') #decorator defines the   
def index():  
    return render_template('index.html', weatherLoc = weatherLoc, weatherURL = weatherUrl, weatherTemp = weatherTemp, 
    time = time, date = date, verse = verse, text = text, station = station, minutes = minutes, homeScore = homeScore, 
    awayScore = awayScore, homeUrl = homeUrl, awayUrl = awayUrl, gameDate = gameDate, stepGoal = stepGoal, name = name, dailySteps = dailySteps,
    activeGoal = activeMinutes, icon = icon, spent = spent, budget = budget, output = output, left = left)  
  
if __name__ =='__main__':  
    app.run(debug = True)  
