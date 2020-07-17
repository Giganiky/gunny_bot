import tweepy
from time import sleep
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import random
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

punkt_param = PunktParameters()
punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc' 'i', 'ii', 'iii', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'etc', 'i.e.', 'e.g.'])
sentence_splitter = PunktSentenceTokenizer(punkt_param)

with open('marx2.txt') as file:
    file_content = file.read()
    file_content = file_content.replace("\n", " ")
    sentences = sentence_splitter.tokenize(file_content)

meows = ("meaaow", "mreahw", "mmaaeh", "mraeww", "mrreeough", "mrahow", "mmriew", "mmmmrrgghh")

for sentence in sentences:
    tweet1 = (random.choice(meows))
    api.update_status(tweet1)
    sleep(14400)
    tweet2 = (random.choice(meows))
    api.update_status(tweet2)
    sleep(14400)
    tweet3 = (random.choice(meows))
    api.update_status(tweet3)
    sleep(14400)
    tweet4 = (random.choice(meows))
    api.update_status(tweet4)
    sleep(14400)
    tweet5 = (random.choice(meows))
    api.update_status(tweet5)
    sleep(14400)
    if len(sentence) > 280:
        x = sentence.split()
        firstpart, secondpart = x[:len(x)//2], x[len(x)//2:]
        separator = ' '
        api.update_status((separator.join(firstpart)))
        sleep(3)
        api.update_status((separator.join(secondpart)))
    else: print(sentence)

    sleep(14400)
