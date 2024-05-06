import requests
from datetime import datetime
MY_LAT = 52.229675
MY_LONG = 21.012230
parameters = {
	"lat": MY_LAT,
	"lng": MY_LONG,
	"formated": 0
}

answer = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
answer.raise_for_status()
data = answer.json()
sunrise = data["results"]["sunrise"].split(':')[0]
sunset = data["results"]["sunset"].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)