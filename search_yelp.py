# -- Simple Yelp - Main Script
# -- Author: Daichi Ishikawa
# -- Written for One Month Python: Week 4 Assignment


from flask import Flask, render_template, request
from yelp_api import yelp_search
import json
import os
from os import environ
from dotenv import load_dotenv, find_dotenv


app = Flask(__name__)

@app.route("/")
def index():
	load_dotenv(find_dotenv())
	user_location = request.values.get("location")
	term = request.values.get("term")
	maps_key = environ['GMAPS_KEY']

	if user_location and term:
		search_results = yelp_search(term, user_location)[:18]
		for result in search_results:
			raw_address = result.location.display_address
			address = ", ".join(raw_address)
			lg_photo = result.image_url
			if lg_photo == None:
				lg_photo = "https://s3-media2.fl.yelpcdn.com/assets/srv0/yelp_styleguide/ef1e928917fa/assets/img/structural/cityscape.png"
			else:
				lg_photo = result.image_url.replace("ms.jpg", "348s.jpg")
			result.image_url = lg_photo
			result.location.display_address = address

			# print(result.location.maps_address) <-- For testing.

		return render_template("index.html", location = user_location, term = term, results = search_results, maps_key = maps_key)

	else:
		results = False
		return render_template("index.html")


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port = port)





