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

	sql = Sql(keyword)
	sql.open()
	sql.createTable()

	scraper = Scraper(keyword)
	scraper.sql = sql
	print("Total count: " +  str(scraper.jobCount))
	scraper.searchForKeyword()

	print("Finished downloading")



if __name__ == "__main__":
	main(sys.argv)