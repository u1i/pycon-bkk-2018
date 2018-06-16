from bottle import default_app, route, request, response, post, run
from random import randint
from datetime import datetime
import json, requests, random

@route('/pycon', method='POST')
def pyconbkk():

    # Capture JSON
    line_json = request.json

    # Get Message and replyToken
    line_token = line_json["events"][0]["replyToken"]
    line_msg = line_json["events"][0]["message"]["text"]

    # Get a random short joke
    sj = [ "Don't trust the atoms - they make up everything", "It's hard to explain puns to kleptomaniacs because they always take things literally.", "Nostalgia ain't what it used to be.", "Is there another word for 'pseudonym'?", "I used to think the brain was the most important organ. Then I thought, look what's telling me that.", "A magician was walking down the street and turned into a grocery store.", "A blind man walks into a bar. And a table. And a chair.", "What's the best part about living in Switzerland? Not sure, but the flag is a big plus.", "Two fish are in a tank. One turns to the other and asks 'How do you drive this thing?'", "Pampered cows produce spoiled milk.", "Learn sign language, it's very handy.", "I started a band called 999 Megabytes - we haven't gotten a gig yet.", "What is the difference between ignorance and apathy? I don't know, and I don't care.", "Dwarfs and midgets have very little in common.", "How do you make Holy Water - you boil hell out of it.", "I wondered why the frisbee was getting bigger, and then it hit me.", "At first I didn't know how to fasten the seatbelt. Then it clicked.", "I totally understand how batteries feel because I'm rarely ever included in things either.", "I invented a new word: Plagiarism" ]

    joke = sj[random.randint(0,len(sj)-1)]

    # Post reply to LINE
    endpoint = "https://api.line.me/v2/bot/message/reply"
    access_token = "PMX4tDO+xS+DdGrGuecmJ+TWxa8VQQ4AgjYAvAxLRr64b9Hu2qxKSIVj6Xh8At0v8mSbxSLfUQdTAkG5hk2HjEdsfHZkDeEuS1x6wcea0EsJ1RaUvqE0VkGGK5Qp7naDf3CneaPN2TO1NPl2lNfAWwdB04t89/1O/w1cDnyilFU="
    send_text = "Hello, what's cooking? Here is a joke you might enjoy: " + joke
    payload = "{\n    \"replyToken\":\"" + line_token + "\",\n    \"messages\":[\n        {\n            \"type\":\"text\",\n            \"text\":\"" + send_text + "\"\n        }\n    ]\n}"
    headers = {
    'Content-Type': "application/json", 'Authorization': "Bearer " + access_token, 'Cache-Control': "no-cache"}

    response = requests.request("POST", endpoint, data=payload, headers=headers)

    return 'OK'
