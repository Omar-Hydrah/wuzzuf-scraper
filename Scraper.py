import requests
import math
from bs4 import BeautifulSoup as Soup
from Job import Job
from Sql import Sql
from multiprocessing import Pool

class Scraper:
	keyword     = ""
	jobCount    = 0
	currentPage = 0
	totalPages  = 0
	baseUrl     = "https://wuzzuf.net/search/jobs/"
	payload     = {"q": "", "start": currentPage}
	sql         = None

	def __init__(self, keyword):
		self.keyword          = keyword
		self.payload["q"]     = keyword
		self.updatePayloadCurrentPage()
		self.getJobCount()

	# Get all the job lists from all pages
	def searchForKeyword(self):
		for i in range(0, self.totalPages + 1):
			self.currentPage = i
			self.updatePayloadCurrentPage()
			jobs = self.getJobList()
			self.saveJobList(jobs)

	def searchForKeywordWithPool(self):
		for i in range(self.totalPages + 1):
			self.currentPage = i
			self.updatePayloadCurrentPage()
			jobs = self.getJobList()

			p1 = Pool(10)
			p2 = Pool(10)
			p1.map(self.saveJob, jobs[0 :10])
			p2.map(self.saveJob, jobs[10:20])


	def saveJob(self, job):
		if self.sql == None:
			raise Exception("Sql object is required to save jobs")

		job = self.getJob(job)
		self.sql.insertJob(job)
		# print(job)

	def saveJobList(self, jobList):
		for job in jobList:
			self.saveJob(job)


	def getJob(self, job):
		
		response   = requests.get(job.url)
		soup       = Soup(response.content, "html.parser")
		salaryInfo = soup.find("dl", {"class": "salary-info"})
		salary     = salaryInfo.find("dd").get_text().strip()
		location   = soup.find("span", 
			{"class": "job-company-location"}).get_text().strip()

		job.salary   = salary
		job.location = location
		return job

	def getJobList(self):
		response = requests.get(self.baseUrl, self.payload)
		soup     = Soup(response.content, "html.parser")
		jobList  = soup.find_all("h2", {"class": "job-title"})
		jobs     = []
		counter  = 0
		for jobItem in jobList:
			jobUrl   = jobItem.find("a").get("href")
			jobTitle = jobItem.get_text().strip() 
			job = Job(self.keyword, jobTitle, None, None, jobUrl)
			counter = counter + 1
			# print(str(counter) + " " + jobTitle)
			# scanJob(job)
			jobs.append(job)

		# Advance to next page
		self.currentPage = self.currentPage + 1
		self.updatePayloadCurrentPage()
		# print("self.payload[start]: " + str(self.payload["start"]))
		# print("self.jobCount: " + str(self.jobCount))
		print("currentPage: " + str(self.currentPage))

		return jobs


	def getJobCount(self):
		response = requests.get(self.baseUrl, self.payload)
		soup     = Soup(response.content, "html.parser")
		count    = soup.find("span", {"class": "search-jobs-count"}).get_text()
		self.jobCount = int(count)
		self.calculateTotalPages()
		print("totalPages: " + str(self.totalPages))

	def calculateTotalPages(self):
		self.totalPages = math.ceil(int(self.jobCount) / 20)
		# self.totalPages = 1
	

	def updatePayloadCurrentPage(self):
		self.payload["start"] = self.currentPage * 10


