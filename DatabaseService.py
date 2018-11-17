import pyodbc

class DatabaseService:
	def __init__(self, connectionString):

		# Open database connection
		self.databaseConnection = pyodbc.connect(connectionString)

		# Create a cursor from the connection
		self.cursor = self.databaseConnection.cursor()

	def get_movies(self, yearFrom, yearTo, category, runtimeFrom, runtimeTo, ratingFrom, movieType, ratingTo):
		#try:
			return self.cursor.execute("exec dbo.usp_GetMovies ?, ?, ?, ?, ?, ?, ?, ?", yearFrom, yearTo, category, runtimeFrom, runtimeTo, ratingFrom, movieType, ratingTo)
		#except Exception as e:
		#	print("\n" + "DatabaseService error :" + "\n" + str(e) + "\n")