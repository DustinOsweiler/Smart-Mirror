import requests

#These are the secrets etc from Fitbit developer
#OAuthTwoClientID = "238GK7"
#ClientOrConsumerSecret = "c8a0a70d79179c2a7efe230e5ce836b8"

accessToken = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhCUlgiLCJzdWIiOiI5WVc4SjciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNjUxODA2NDQ2LCJpYXQiOjE2NTEyMDE3MzZ9.Sk3p6rjBcd4z_QkFtsw1DDg1riCvR_aPwWUjKUNnNf4"

header = {'Authorization': 'Bearer {}'.format(accessToken)}
response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()

#print(response['user'])

user = response['user']

header = {'Authorization': 'Bearer {}'.format(accessToken)}
response = requests.get("https://api.fitbit.com/1/user/-/activities/goals/daily.json", headers=header).json()

#print(response)
goals = response['goals']
activegoal = goals['activeMinutes']
stepGoal = goals['steps']

Name = user['fullName']
dailySteps = user['averageDailySteps']
icon = user['avatar']


#This is the Fitbit URL
#TokenURL = "https://api.fitbit.com/oauth2/token"

#I got this from the first verifier part when authorising my application
#AuthorizationCode = "https://www.fitbit.com/oauth2/authorize"

#Form the data payload
#BodyText = {'code' : AuthorizationCode,
#            'redirect_uri' : 'http://127.0.0.1:5000/',
#            'client_id' : OAuthTwoClientID,
#            'grant_type' : 'authorization_code'}

#BodyURLEncoded = urllib.urlencode(BodyText)
#print(BodyURLEncoded)

#Start the request
#req = urllib2.Request(TokenURL,BodyURLEncoded)

#Add the headers, first we base64 encode the client id and client secret with a : inbetween and create the authorisation header
#req.add_header('Authorization', 'Basic ' + base64.b64encode(OAuthTwoClientID + ":" + ClientOrConsumerSecret))

 

#req.add_header('Content-Type', 'application/x-www-form-urlencoded')

#Fire off the request
#try:
#  response = urllib2.urlopen(req)

#  FullResponse = response.read()

#  print("Output >>> ") + FullResponse
#except urllib2.URLError as e:
#  print(e.code)
#  print(e.read())