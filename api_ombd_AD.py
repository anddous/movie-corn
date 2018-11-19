import requests
import json
import sys
title = sys.argv[row.movie] 
rok = sys.argv[row.rok]

dotaz = requests.get('http://www.omdbapi.com/?apikey=c206c397&t=' + title + '&y=' + rok)
filmy = json.loads(dotaz.text)
herci = filmy['Actors']
anotace = filmy['Plot']
poster = filmy['Poster']
reziser = filmy['Director']
print(herci)
print(anotace)
print(poster)
print(reziser)
# Co vrací API?
#print(filmy.keys())

''' 
FUNKČNÍ ZÁPIS DO JSON SOUBORU
json = json.dumps(filmy)
f = open("omdb.json","w")
f.write(json)
f.close()
'''