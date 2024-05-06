import requests
import twilio
import datetime

STOCK = "TM"
COMPANY_NAME = "Toyota Motor Corporation"
api_key = "FL8PEMWDK37NMYUC"
news_api_key = "17ff89518a33474e8e52ce0f6291da8f"
parameters = {
	"function": 'TIME_SERIES_DAILY',
	"symbol": 'TM',
	"apikey": api_key,
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
# response = requests.get('https://www.alphavantage.co/query', params=parameters)
# response.raise_for_status()
# data = response.json()['Time Series (Daily)']
#
# today = datetime.date.today()
#
# diff = 1
# if today.weekday() == 0:
# 	diff = 3
# elif today.weekday() == 6:
# 	diff = 2
# else:
# 	diff = 1
#
# yesterday = today - datetime.timedelta(diff)
#
# if yesterday.weekday() == 0:
# 	yesterday_diff = 3
# elif yesterday.weekday() == 6:
# 	yesterday_diff = 2
# else:
# 	yesterday_diff = 1
#
# day_before_yesterday = yesterday - datetime.timedelta(yesterday_diff)
#
# yesterday_price = float(data[f'{yesterday}']['4. close'])
# day_before_yesterday_price = float(data[f'{day_before_yesterday}']['4. close'])
#
# close_percentage = (yesterday_price-day_before_yesterday_price)/day_before_yesterday_price * 100
#
# print(close_percentage)
#
# if 5 < close_percentage < 6:
# 	print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_params = {
	"apiKey": news_api_key,
	"q": "Toyota Motors OR Toyota",
	"searchIn": "title",
	"sortby": "popularity",
	"pageSize": 3,
	"sortBy": "popularity",
	"language": "en",
}
news_request = requests.get('https://newsapi.org/v2/everything', params=news_params)
news_request.raise_for_status()
news_data = news_request.json()
print(news_data)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
