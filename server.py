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

# natažení stránky movie
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

	# Connect to the database
	database = DatabaseService(connectionString)
	cursor = database.get_movies(yearFrom, yearTo)


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



