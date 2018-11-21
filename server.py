from flask import Flask, render_template, g, Blueprint, url_for, request, redirect, jsonify
import logging
#from jinja2 import exceptions
#from flaskext.mysql import MySQL
#from openpyxl.reader.excel import load_workbook
from DatabaseService import DatabaseService
# zavolání třídy ApiService
#from ApiService import ApiService
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
	tconst = request.args.get('tconst')
	# spusteni procedury, ktera nam vrati nazev filmu, rok (vstupni parametr do procedury je tconst)
	# spusteni ombd API a ziskani ostatnich udaju vcetne adresy na obrazek
	# vraceni sablony vcetne ziskanych informaci
	return render_template("detail_m.html", tconst=tconst)

#@movieCorn.route("/api/search/<year>")
#def GetSearchResult(year):
#  return render_template("registrace.html")

# https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url
@movieCorn.route("/api/search")
def search():
	year = request.args.get('year')

	if year == "vše" or year == "rok":
		yearFrom = 1950
		yearTo = 9999	
	elif "-" in year: 
		yearFrom = year[:4]
		yearTo = year[-4:]
	else: # ...
		yearFrom = year[:4]
		yearTo = 9999

	# @category
	category = request.args.get('category')
	#	movieCorn.logger.info('category: %s', category)
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
		category = None

	# @runtime
	runtime = request.args.get('runtime')
	runtimeFrom = 0
	if runtime == ' <60 min.': 
		runtimeTo = 60
	elif runtime == ' <90 min.': 
		runtimeTo = 90
	elif runtime == ' <120 min.': 
		runtimeTo = 120
	elif runtime == ' >120 min.': 
		runtimeFrom = 120
		runtimeTo = None	
	else: 
		runtimeTo = None

	# movieType
	movieType = request.args.get('movietype')

	if movieType == 'seriál':
		movieType = 'serial'
	elif movieType == 'film':
		movieType = 'film'
	else:
		movieType = None

	# @rating
	rating = request.args.get('rating')
	if rating == '<=5.0': 
		ratingFrom = 0
		ratingTo = 5
	elif rating == '<=7.0': 
		ratingFrom = 5
		ratingTo = 7
	elif rating == '<=8.0': 
		ratingFrom = 7
		ratingTo = 8
	else: 
		ratingFrom = None
		ratingTo = None

	tconst = request.args.get('tconst')

	# Connect to the database
	database = DatabaseService(connectionString)
	cursor = database.get_movies(yearFrom, yearTo, category, runtimeFrom, runtimeTo, movieType, ratingFrom, ratingTo, tconst)
	html = "<div class='row'>"
	for row in cursor.fetchall():
		html = html + """<div class="col-md-4" style="color:black; margin-top: 10px">
					<div class="card" style="width: 18rem; background-color:#ddd">
							<div class="card-body">"""
		html = html + "<h5 class='card-title'>"+ str(row.movie) + "</h5>"
		html = html + """<p class="card-text">
											Genre: """ + str(row.genre) +"""<br>Year: """ + str(row.startY) + """<br>Country: """+ str(row.country) + """ <br>Rating: """ + str(row.stars) + """<br>Typ: """+ str(row.tType) + """</p> 
										<a href="/detail_m?tconst=""" + str(row.tconst) +"""" class="btn" style="background-color:#353A41; color:white">Detail</a>
							</div>
						</div>
			</div>"""
	html = html + "</div>"

	return html

movieCorn.run(debug=True)



