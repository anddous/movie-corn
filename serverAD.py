from flask import Flask, render_template, g, Blueprint, url_for, request, redirect, jsonify
#from jinja2 import exceptions
#from flaskext.mysql import MySQL
#from openpyxl.reader.excel import load_workbook
from DatabaseService import DatabaseService
movieCorn = Flask(__name__)

connectionString = "DRIVER={SQL Server};SERVER=DESKTOP-EII5KB0\SQLEXPRESS;DATABASE=MovieCorn;Trusted_Connection=yes;"

# natažení home-page index
@movieCorn.route('/', methods=['GET'])
def index():
	return render_template('index.html')

# natažení stránky registrace
@movieCorn.route("/registrace")
def registrace():
  return render_template("registrace.html")

# natažení stránky prihlaseni
@movieCorn.route("/prihlaseni")
def prihlaseni():
  return render_template("prihlaseni.html")

	# natažení stránky detail-movie
@movieCorn.route("/detail_m")
def detail_m():
  return render_template("detail_m.html")

#@movieCorn.route("/api/search/<year>")
#def GetSearchResult(year):
#  return render_template("registrace.html")

''' Funkcni reseni, vraci JSON
# https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url
@movieCorn.route("/api/search")
def search():
	
	year = request.args.get('year')
	yearFrom = year[:4]
	if year.find("-"):
			yearTo = year[-4:]
	else: # ...
			yearTo = 9999

	# Connect to the database
	database = DatabaseService(connectionString)
	cursor = database.get_movies(yearFrom, yearTo)

	output = []
	for row in cursor.fetchall():
		output.append(row.originalTitle)

	return jsonify(output)
'''

# https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url
@movieCorn.route("/api/search")
def search():
	
	year = request.args.get('year')
	#category = request.args.get('category')

	if year == "vše" or year == "rok":
		yearFrom = 1950
		yearTo = 9999	
	elif "-" in year: 
		yearFrom = year[:4]
		yearTo = year[-4:]
	else: # ...
		yearFrom = year[:4]
		yearTo = 9999

	# nový kód ANDREA
	# @category
	category = request.args.get('category')
	if category == 'komedie': 
		category = 'Comedy'
	elif category == 'krimi': 
		category = 'Crime'
	elif category == 'thriller': 
		category = 'Thriller'
	elif category == 'horor': 
		category = 'Horror'
	elif category == 'akční': 
		category = 'Action'
	elif category == 'romantika': 
		category = 'Romance'
	elif category == 'animované': 
		category = 'Animation'
	elif category == 'fantasy':
		category = 'Fantasy'
	elif category == 'sci-fi':
		category = 'Sci-fi'
	elif category == 'drama':
		category = 'Drama'
	elif category == 'dobrodružné':
		category = 'Adventure'
	elif category == 'historie':
		category = 'History'
	elif category == 'western':
		category = 'Western'
	else:
		category = '%'

# @runtime
runtime = request.args.get('runtime')
	if runtime == "vše" or runtime == "délka":
		runtimeFrom = 0
		runtimeTo = 100000000
	elif runtime == '<60 min.': 
		runtimeFrom = 0
		runtimeTo = 59
	elif runtime == '<90 min.': 
		runtimeFrom = 0
		runtimeTo = 89
	elif runtime == '<120 min.': 
		runtimeFrom = 0
		runtimeTo = 119
	else: 
		runtimeFrom = 120
		runtimeTo = 10000000000

# movieType = request.args.get('movieType')
if movieType == 'seriál':
	movieType = 'null'
elif movieType == 'film':
	movieType = ''

# @rating
rating = request.args.get('rating')
	if rating == "vše" or year == "rating":
		ratingFrom = 0
		ratingTo = 100
	elif rating == '<=5.0': 
		ratingFrom = 0
		ratingTo = 5.0
	elif rating == '<=7.0': 
		ratingFrom = 5.1
		ratingTo = 7.0
	elif rating == '<=8.0': 
		ratingFrom = 7.1
		ratingTo = 8.0
	else: 
		runtimeFrom = 8.1
		ratingTo = 100

	# Connect to the database
	database = DatabaseService(connectionString)
	cursor = database.get_movies(yearFrom, yearTo, category, runtimeFrom, runtimeTo, movieType, ratingFrom, ratingTo)

	html = "<div class='row'>"
	for row in cursor.fetchall():
		html = html + """<div class="col-md-4" style="color:black; margin-top: 10px">
					<div class="card" style="width: 18rem; background-color:#ddd">
							<div class="card-body">"""
		html = html + "<h5 class='card-title'>"+ str(row.movie) + "</h5>"
		html = html + """<p class="card-text">Tady bude anotace k filmu. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
								<a href="#" class="btn" style="background-color:#353A41; color:white">Detail filmu</a>
							</div>
						</div>
			</div>"""
	html = html + "</div>"

	return html





movieCorn.run(debug=True)



