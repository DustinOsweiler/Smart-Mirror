import requests
import json
import APIs.Time as Time
#import Time

header = { 
  "apikey": "ce14f140-c69c-11ec-b6b6-3dc5d45ec945"}

param = {
   ("league_id","663"),
}

response = requests.get('https://app.sportdataapi.com/api/v1/soccer/seasons', headers=header, params=param)
leaguestuff = json.loads(response.text)
#print(leaguestuff)

seasonid = 0

seasondata = leaguestuff['data']

for data in seasondata:
    if data['is_current'] == 1:
        seasonid = data['season_id']

#print(seasonid)

headers = { 
  "apikey": "ce14f140-c69c-11ec-b6b6-3dc5d45ec945"}

params = {
   ("season_id", seasonid),
   ("date_to", Time.date)
}

response = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=headers, params=params)
soccer = (response.text)

listofgames = []

unprocessedsoccer = json.loads(soccer)
unprocessedsoccer = unprocessedsoccer['data']
for i in unprocessedsoccer:
  hometeam = (i['home_team'])
  if int(hometeam['team_id']) == 8004:
    listofgames.append(i)
  awayteam = (i['away_team'])
  if int(awayteam['team_id']) == 8004:
    listofgames.append(i)

#print(listofgames[0])
listofgames.sort(key=lambda b: b['match_id'], reverse=True)
#print(listofgames)

recentGame = listofgames[0]

gameStats = recentGame['stats']

homeStats = recentGame['home_team']
homeLogo = homeStats['logo']
homeScore = gameStats['home_score']

awayStats = recentGame['away_team']
awayLogo = awayStats['logo']
awayScore = gameStats['away_score']

GameDate = recentGame['match_start']
GameDate = GameDate.split(" ")[0]

def getSoccer():
  header = { 
  "apikey": "ce14f140-c69c-11ec-b6b6-3dc5d45ec945"}

  param = {
    ("league_id","663"),
  }

  response = requests.get('https://app.sportdataapi.com/api/v1/soccer/seasons', headers=header, params=param)
  leaguestuff = json.loads(response.text)
  #print(leaguestuff)

  seasonid = 0

  seasondata = leaguestuff['data']

  for data in seasondata:
    if data['is_current'] == 1:
      seasonid = data['season_id']

  #print(seasonid)

  headers = { 
    "apikey": "ce14f140-c69c-11ec-b6b6-3dc5d45ec945"}

  params = {
    ("season_id", seasonid),
    ("date_to", Time.date)
  }

  response = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=headers, params=params)
  soccer = (response.text)

  listofgames = []

  unprocessedsoccer = json.loads(soccer)
  unprocessedsoccer = unprocessedsoccer['data']
  for i in unprocessedsoccer:
    hometeam = (i['home_team'])
    if int(hometeam['team_id']) == 8004:
      listofgames.append(i)
    awayteam = (i['away_team'])
    if int(awayteam['team_id']) == 8004:
      listofgames.append(i)

  #print(listofgames[0])
  listofgames.sort(key=lambda b: b['match_id'], reverse=True)
  #print(listofgames)

  recentGame = listofgames[0]

  gameStats = recentGame['stats']

  homeStats = recentGame['home_team']
  homeLogo = homeStats['logo']
  homeScore = gameStats['home_score']

  awayStats = recentGame['away_team']
  awayLogo = awayStats['logo']
  awayScore = gameStats['away_score']

  GameDate = recentGame['match_start']
  GameDate = GameDate.split(" ")[0]

  return(homeLogo, homeScore, awayLogo, awayScore, GameDate)
#print(awayLogo, homeLogo)

#print(awayStats, homeStats)

#print(Time.date)

#print(soccer)

#print(recentGame)

#print(listofgames)

#print(GameDate)

#print(homeScore, awayScore)

#<div id="wg-api-football-standings"
#        data-host="v3.football.api-sports.io"
#        data-league="39"
#        data-team=""
#        data-season="2020"
#        data-key="Your-Api-Key-Here"
#        data-theme="0023c6c134mshfe6d1aea7cba72fp156c83jsn71912b0b2f43"
#        -show-errors="false"
#        class="api_football_loader"></div>
#        <script
#          type="module"
#          src="https://widgets.api-sports.io/football/1.1.8/widget.js">
#        </script>
#      </div>