class Job:

	category = ""
	company  = ""
	salary   = ""
	location = ""


	def __init__(self, category, job, salary=None, company=None, url=None):
		self.category = category
		self.job      = job
		self.salary   = salary
		self.company  = company
		self.url      = url

