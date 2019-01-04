class HtmlCreator:
	title = ""
	file  = None
	titleTag = "<title>%s</title>"
	upperContent = """<!DOCTYPE html>
		<html>
		<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="initial-scale=1, device-width=1" />
		<link rel="stylesheet" type="text/css" href="materialize.min.css">"""

	middleContent = """</head>
		<body><div class='container'>"""

	lowerContent = """
	</div>
	<script type="text/javascript" src="jquery.min.js"></script>
	<script type="text/javascript" src="materialize.min.js"></script>
	</body>
	</html>"""
	table = None
	jobs  = None


	def __init__(self, title, jobs):
		self.jobs  = jobs
		self.title = title
		self.file = open(title + ".html", "w")
		self.write(self.upperContent)
		self.write(self.titleTag % self.title)
		self.write(self.middleContent)
		self.createTable()
		# self.insertTableData()
		self.write(self.table)
		self.close() # Write the </body></html> tags


	def createTag(self, tag, content):
		return "<%s>%s</%s>" % (tag, content, tag)

	def createJobRow(self, job):
		tableRow = """<tr>
			<td><a href='%s' target='_blank'>%s</a></td>
			<td>%s</td><td>%s</td></tr>""" % (job.url, job.title, 
				job.salary, job.location) 
		return tableRow

	def createTableRowList(self):
		rowList = ""
		for job in self.jobs:
			rowList = rowList + "\n" + self.createJobRow(job)
		return rowList
			
	def insertTableData(self):
		self.table = self.table % self.createTableRowList()

	def createTable(self):
		self.table = """<table>
			<thead>
				<tr>
					<th>Title</th>
					<th>Salary</th>
					<th>Location</th>
				</tr>
			</thead>
			<tbody>
				%s
			</tbody>
		</table>""" % self.createTableRowList()
		# return table


	def write(self, content):
		self.file.write(content)


	def close(self):
		self.write(self.lowerContent)
		self.file.close()

