import requests
from twilio.rest import Client

account_sid = "ACe38f1bd1b6a5da5da77297b4acbf4c7d"
auth_token = "276cfd02ca5e11ff7659bd77413f7be8"

parameters = {
	"appid": "f1eb7151655517d04188cf8e7423b6bc",
	"lat": 52.229675,
	"lon": 21.012230,
	"cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
	condition_code = hour_data["weather"][0]["id"]
	if int(condition_code) < 700:
		will_rain = True
if will_rain:
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		body="Lalala Papapap",
		from_= '+19186094728',
		to='+48501501519',
	)
else:
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		body="Mamma Mia",
		from_= '+19186094728',
		to='+48501501519',
	)
print(message.status)

