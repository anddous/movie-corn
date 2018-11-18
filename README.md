# movie-corn

PY SOUBORY:
Funkční soubory po hackatlonu - funkční filtry pouze na rok:
- server_Lukas.py
- DatabaseServis_Lukas.py

Verze s dopracovanými filtry, ale zatím nefungují:
- server.py
- DatabaseServis.py

TEMPLATES:
Index.html
- změny od hacktlonu - u filtrů dopsané ID
- přidán odkaz na novou hmtl stránku (struktura pro detail filmu) - název: Detail_m (do hlavičky webu, abych si stránku mohla vyzkoušet, jak vypadá)

SQL queries obsahuje:
- zkušební pro dotazy v SQL
- upravená procedura pro další filtry:
AD_AD_dbo-get-movies- procedura_pokus1.sql

- původní Lukášova procedura z hackatlonu:
dbo-get-movies-procedura.sql

API pro další informace k filmů:
- omdb.py
- ombd1.py - dopsané do sys.argv odkazy na výsledky z hledání, zatím dále nerozpracováno dále

API pro info, kde filmy běží + kde stáhnout film + titulky
	TV program - xml 
	https://www.ceskatelevize.cz/xml/tv-program/

	Hledání ulozto:	 - hledání "The Row 2018"
	https://uloz.to/hledej?q=The+Row+2018&type=videos

	Titulky.com - hledání "nemo"
	https://www.titulky.com/?Fulltext=nemo

	Opensubtitles.org - hledání "nemo" - cz + slove
	https://www.opensubtitles.org/cs/search2/sublanguageid-cze,slo/moviename-nemo








