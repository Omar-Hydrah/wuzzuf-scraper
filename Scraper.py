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

	def __init__(self, keyword):
		self.keyword = keyword
		# Scan first page to get total count of jobs
		# Get the totalPages count
		# Scan every page get with getJobList()
		# Save every job on the list with saveJob() 

	def saveJob(self, url):
		# title = jobItem.get_text().strip()
		# url  = jobItem.find("a").get("href")

		# jobSoup = getJobSoup(url)
		# salary  = getJobSalary(jobSoup)
		# job = Job(keyword, title, salary, None, url)

		# sql.insertJob(job)
		# print(title)
	

	def scanPage(self, url, payload):


	def scanPagesForJob(self, job):
		# baseUrl = "https://wuzzuf.net/search/jobs/?q="
		# url     = baseUrl + job
		url = "https://wuzzuf.net/search/jobs/"

		# Scanning for initial jobs count
		soup = getJobListSoup(url, params={"q": job})

		pageCounter = 0
		jobsCount   = getNumberOfJobs(soup)
		totalPages  = math.ceil(jobsCount / 20) 
		

		payload = {"q": job, "start": pageCounter * 10}
		print("Sanning " + str(totalPages) + " pages.")

		for i in range(0, totalPages + 1):

			pageCounter = pageCounter + 1
			payload["start"] = pageCounter

			soup = getJobListSoup(url, payload)





	def getJobListSoup(self, url, payload = None):
		response = requests.get(url, params=payload)
		soup     = Soup(response.content, "html.parser")
		return soup

	def getJobListFromSoup(self, soup):

		jobList = soup.find_all("h2", {"class": "job-title"})

		return jobList

	def getJobSoup(self, url):
		response = requests.get(url)
		soup     = Soup(response.content, "html.parser")

		return soup

	def getJobSalary(self, soup):

		salaryInfo = soup.find("dl", {"class": "salary-info"})
		salary     = salaryInfo.find("dd").get_text().strip()

		return salary

	def getNumberOfJobs(self, soup):

		count = soup.find("span", {"class": "search-jobs-count"}).get_text()

		return count
