from flask import Flask, render_template, g, Blueprint, url_for, request, redirect, jsonify
from DatabaseService import DatabaseService

# https://help.parsehub.com/hc/en-us/articles/217751808-API-Tutorial-How-to-get-run-data-using-Python-Flask

# pouze slátanina - soubor api-test.py - funguje - propisuje údaje z api, ale jak to implementovat do metody a stránky detail?
class ApiService:
	def requestApi(self, r):
			self.r = requests.get('http://www.omdbapi.com/?apikey=c206c397&t=Terminator&y=1984')
	movies = r.json()
	return movies['Plot']