# -- Simple Yelp - Yelp Api Functions
# -- Author: Daichi Ishikawa
# -- Written for One Month Python: Week 4 Assignment


from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from os import environ
from pprint import pprint
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
    consumer_key = environ['YELP_CONSUMER_KEY'],
    consumer_secret = environ['YELP_CONSUMER_SECRET'],
    token = environ['YELP_TOKEN'],
    token_secret = environ['YELP_TOKEN_SECRET']
)

client = Client(auth)

def yelp_search(term, location):

	params = {
	    'term': term,
	    'lang': 'en',
	}
	response = client.search(location, **params).businesses
	return response


def business_details(id):
	params = {
    	'lang': 'en',
    	'actionlinks': True
	}
	response = client.get_business(id, **params).business
	return response