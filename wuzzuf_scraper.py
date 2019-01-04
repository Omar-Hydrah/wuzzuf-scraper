import requests
import re
import argparse
import sys
import math
import sqlite3 as sqlite
from bs4 import BeautifulSoup as Soup
from Job import Job
from Sql import Sql
from Scraper import Scraper


def main(argv):

	parser = argparse.ArgumentParser()
	parser.add_argument("-k", "--keyword", help="The keyword to search for on wuzzuf")

	args = parser.parse_args()

	keyword = args.keyword  
	# baseUrl = "https://wuzzuf.net/search/jobs/?q="
	# url     = baseUrl + keyword

	# soup    = getJobListSoup(url)
	# jobList = getJobListFromSoup(soup)

	sql = Sql(keyword)
	sql.open()
	sql.createTable()

	scraper = Scraper(keyword)
	print("Total count: " +  str(scraper.jobCount))
	jobs = scraper.getJobList()
	for job in jobs:
		# print(job)
		# print(job.title)
		# print(job.url)
		pass

	# for jobItem in jobList:
	# 	# print(jobItem.get_text().strip())
	# 	# print(jobItem.find("a").get("href"))
	# 	title = jobItem.get_text().strip()
	# 	url  = jobItem.find("a").get("href")

	# 	jobSoup = getJobSoup(url)
	# 	salary  = getJobSalary(jobSoup)
	# 	job = Job(keyword, title, salary, None, url)

	# 	sql.insertJob(job)
	# 	print(title)


	print("Finished downloading")



if __name__ == "__main__":
	main(sys.argv)