class Job:

	category = ""
	company  = ""
	salary   = ""



	def __init__(self, category, job, salary, company=None, url=None):
		self.category = category
		self.job      = job
		self.salary   = salary
		self.company  = company
		self.url      = url

