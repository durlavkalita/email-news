import requests
import os
from dotenv import load_dotenv
from send_mail import send_mail

topic = 'cricket'

load_dotenv()

api_key = os.getenv('API_KEY')
url = "https://newsapi.org/v2/everything?"\
    "q="+topic+"&sortBy=publishedAt&"\
    "apiKey="+api_key+"&language=en"

request = requests.get(url)
content = request.json()


body = "Subject: Today's news" + "\n"

try:
  for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
      body = body + article['title'] + '\n' + article["description"]  + '\n' + article['url'] + '\n' + 2*'\n'
except:
  body = body + "Error occurred when fetching news"

body = body.encode('utf-8')

try:
  send_mail(message = body)
except:
  print('Could not send mail')