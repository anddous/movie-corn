import pyodbc

class DatabaseService:
	def __init__(self, connectionString):

		# Open database connection
		self.databaseConnection = pyodbc.connect(connectionString)

		# Create a cursor from the connection
		self.cursor = self.databaseConnection.cursor()

	def get_movies(self, yearFrom, yearTo):
		#try:
			return self.cursor.execute("exec dbo.usp_GetMovies ?, ?", yearFrom, yearTo)
		#except Exception as e:
		#	print("\n" + "DatabaseService error :" + "\n" + str(e) + "\n")