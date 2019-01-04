import requests
import math
from bs4 import BeautifulSoup as Soup
from Job import Job
from Sql import Sql

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
		# self.payload["start"] = self.currentPage * 10
		self.updatePayloadCurrentPage()
		self.getJobCount()
		# Scan first page to get total count of jobs
		# Get the totalPages count
		# Scan every page get with getJobList()
		# Save every job on the list with saveJob() 

	# Get all the job lists from all pages
	def scanFullJobList(self):
		for i in range(0, self.totalPages + 1):
			self.currentPage = i
			self.updatePayloadCurrentPage()
			jobs = self.getJobList()
			self.saveJobList(jobs)


	def saveJob(self, job):
		if self.sql == None:
			raise Exception("Sql object is required to save jobs")

		self.sql.insertJob(job)

	def saveJobList(self, jobList):
		for job in jobList:
			saveJob(job)

	def getJob(self, job):
		
		# title = jobItem.get_text().strip()
		# url  = jobItem.find("a").get("href")

		# jobSoup = getJobSoup(url)
		# salary  = getJobSalary(jobSoup)
		# job = Job(keyword, title, salary, None, url)

		# sql.insertJob(job)
		# print(title)
		response   = requests.get(job.url)
		soup       = Soup(response.content, "html.parser")
		salaryInfo = soup.find("dl", {"class": "salary-info"})
		salary     = salaryInfo.find("dd").get_text().strip()

		job.salary = salary
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
			print(str(counter) + " " + jobTitle)
			# scanJob(job)
			jobs.append(job)

		# Advance to next page
		self.currentPage = self.currentPage + 1
		self.updatePayloadCurrentPage()
		print("Payload-Start: " + str(self.payload["start"]))

		return jobs



	def calculateTotalPages(self):
		# self.totalPages = self.jobCount / 20
		self.totalPages = 2
	
	def getJobCount(self):
		response = requests.get(self.baseUrl, self.payload)
		soup     = Soup(response.content, "html.parser")
		count    = soup.find("span", {"class": "search-jobs-count"}).get_text()
		self.jobCount = int(count)
		# print(type(count))
		# print(count)
		self.calculateTotalPages()
		print("totalPages: " + str(self.totalPages))


	def updatePayloadCurrentPage(self):
		self.payload["start"] = self.currentPage * 10


