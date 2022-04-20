from flask import Flask 
from flask import Flask, render_template
import Time
import Bible
#import Gas
import Soccer
import Weather

app = Flask(__name__) #creating the Flask class object   

time = Time.time
date = Time.date
verse = Bible.Bible
#gasprice = Gas.gas
soccerstats = Soccer.soccer
weather = Weather.weather

 
@app.route('/') #decorator defines the   
def index():  
    return render_template('index.html', time = time, date = date, verse = verse, soccerstats = soccerstats, weather = weather);  
  
if __name__ =='__main__':  
    app.run(debug = False)  