class Job:

	category = ""
	company  = ""
	salary   = ""
	location = ""
	title    = ""


	def __init__(self, category, title, salary=None, company=None, url=None, 
		location=None):
		self.category = category
		self.title      = title
		self.salary   = salary
		self.company  = company
		self.url      = url
		self.location = location

	def __str__(self):
		return "{category: %s, title: %s, salary: %s, company: %s, location : %s}" % (
			self.category, self.title, self.salary, self.company, self.location)