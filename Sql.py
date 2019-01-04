import sqlite3 as sqlite
import Job

class Sql():
	database   = ""
	connection = ""
	cursor     = ""

	def __init__(self, database):
		self.database   = database
		# self.connection = sqlite.connect(database + ".db")
		# self.cursor     = self.connection.cursor()

	def open(self):
		self.connection = sqlite.connect(self.database + ".db")
		self.cursor     = self.connection.cursor()


	def createTable(self):
		query = """create table if not exists jobs
			(id integer primary key autoincrement, 
			category text, job text, salary text, company text, url text)"""
		self.cursor.execute(query)
		self.connection.commit()

	def insertJob(self, job):
		query = """insert into jobs(category, job, salary, company, url) 
			values(?, ?, ?, ?, ?)"""
		self.cursor.execute(query, (job.category, job.job, job.salary, 
			job.company, job.url))
		self.connection.commit()



	def close(self):
		self.cursor.close()
		self.connection.close()