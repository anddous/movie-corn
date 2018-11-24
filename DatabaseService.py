import pyodbc

class DatabaseService:
	def __init__(self, connectionString):

		# Open database connection
		self.databaseConnection = pyodbc.connect(connectionString)

		# Create a cursor from the connection
		self.cursor = self.databaseConnection.cursor()

	def get_movies(self, yearFrom, yearTo, category, runtimeFrom, runtimeTo, movieType, ratingFrom, ratingTo, tconst):
		#try:
			return self.cursor.execute("exec dbo.usp_GetMovies ?, ?, ?, ?, ?, ?, ?, ?, ?", yearFrom, yearTo, category, runtimeFrom, runtimeTo, movieType, ratingFrom, ratingTo, tconst)
	def get_movie(self, tconst):
			return self.cursor.execute("SELECT * FROM [MovieCorn].[imdb].[Movie] as mov join imdb.Region as reg on reg.titleId =mov.tconst join imdb.Rating as rat on rat.tconst = mov.tconst WHERE mov.tconst = ?", tconst)
		#except Exception as e:
		#	print("\n" + "DatabaseService error :" + "\n" + str(e) + "\n")