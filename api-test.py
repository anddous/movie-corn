from flask import Flask, render_template, g, Blueprint, url_for, request, redirect, jsonify
import json
import requests

#from ApiService import ApiService

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def Api():
	#params = { 
	#'searchMovie': '{Terminator}', 'searchYear': '{1984}' }
	#r = request.get_data('http://www.omdbapi.com/?apikey=c206c397&t={0}&y={1}', params=params)
	r = requests.get('http://www.omdbapi.com/?apikey=c206c397&t=Terminator&y=1984')
	movies = r.json()
	return movies['Plot']
	#return r.text

app.run(debug=True)


'''
def homepage():
  params = {
    'api_key': '{API_KEY}',
  }
  r = requests.get(
      'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
      params=params)
  return render_template('movies.html', movies=json.loads(r.text)['movies'])

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

		for movie in movies:
			actor = movies['Actors']
			plot = movies['Plot']
			director = movies['Director']
			poster = movies['Poster'] 

	g = urllib2.urlopen(query_url)
    results = g.read()
    g.close()

    data = json.loads(results)

'''