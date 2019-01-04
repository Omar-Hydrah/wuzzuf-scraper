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
from HtmlCreator import HtmlCreator

def downloadJobs(keyword, sql):
	scraper = Scraper(keyword)
	scraper.sql = sql
	print("Jobs count: " +  str(scraper.jobCount))
	scraper.searchForKeyword()

	print("Finished downloading")

def writeHtmlFile(keyword, sql):
	jobs = sql.getJobs()
	# print(len(jobs))
	# print(jobs[0])
	# print(jobs[1])
	html = HtmlCreator(keyword, jobs)
	print("File written")

def main(argv):

	parser = argparse.ArgumentParser()
	parser.add_argument("-k", "--keyword", help="The keyword to search for on wuzzuf")
	parser.add_argument("-a", "--action", help="Action <download | write>")

	args = parser.parse_args()

	keyword = args.keyword
	action  = args.action

	sql = Sql(keyword)
	sql.open()
	sql.createTable()

	if action == "download":
		downloadJobs(keyword, sql)
	elif action == "write":
		writeHtmlFile(keyword, sql) 
	else:
		print("Missing --action to jobs; to download or write them to html")


if __name__ == "__main__":
	main(sys.argv)