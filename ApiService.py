import pyodbc
import requests
import json
import sys

# https://help.parsehub.com/hc/en-us/articles/217751808-API-Tutorial-How-to-get-run-data-using-Python-Flask

class ApiService:
	def queryApi(self, result):
		self.result = requests.get('http://www.omdbapi.com/?apikey=c206c397&t={row.movie}&y={row.startY}')
		return render_template('detail_m.html', movies=json.loads(result.text)['movies'])
