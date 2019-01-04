class Job:

	category = ""
	company  = ""
	salary   = ""
	location = ""


	def __init__(self, category, job, salary=None, company=None, url=None, location=None):
		self.category = category
		self.job      = job
		self.salary   = salary
		self.company  = company
		self.url      = url
		self.location = location

	def __str__(self):
		return "{category: %s, job: %s, salary: %s, company: %s, location : %s}" % (
			self.category, self.job, self.salary, self.company, self.location)