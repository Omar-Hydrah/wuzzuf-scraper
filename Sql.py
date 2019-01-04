import sqlite3 as sqlite
from Job import Job

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
			category text, title text, salary text, company text, 
			location text, url text)"""
		self.cursor.execute(query)
		self.connection.commit()

	def insertJob(self, job):
		query = """insert into jobs(category, title, salary, company, url, location) 
			values(?, ?, ?, ?, ?, ?)"""
		self.cursor.execute(query, (job.category, job.title, job.salary, 
			job.company, job.url, job.location))
		self.connection.commit()

	def getJobs(self):
		query = "select * from jobs"
		self.cursor.execute(query)
		jobResults = self.cursor.fetchall()
		jobs = []

		for result in jobResults:
			job = Job(result[1], result[2], result[3], 
				result[4],  result[6], result[5])
			jobs.append(job)

		return jobs

	def close(self):
		self.cursor.close()
		self.connection.close()