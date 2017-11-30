import cherrypy
import re
import json
from _salaries_database import _salaries_database

class EmployeeController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self):
		output = {'result':'success'}
		ldict = []
		try:
			employee_ids = self.sdb.get_employees()
			for eid in employee_ids:
				templist = self.sdb.get_employee(eid)
				tempdict = {}
				tempdict['id'] = templist[0]
				tempdict['name'] = templist[1]
				tempdict['jobtitle'] = templist[2]
				tempdict['basepay'] = templist[3]
				tempdict['totalpay'] = templist[4]
				tempdict['year'] = templist[5]
				tempdict['agency'] = templist[6]		
				ldict.append(tempdict)
			output['employees'] = ldict
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

""" NOT SURE ABOUT THIS PART / HOW YOU ARE USING SET EMPLOYEE """
	def POST(self):
		output = {'result':'success'}
		the_body = cherrypy.request.body.read().decode()
		eidl = []
		try:
			the_body = json.loads(the_body)
			employee_ids = self.sdb.get_employees()
			for employee_id in employee_ids:
				eidl.append(int(employee_id))
			eid = max(eidl) + 1
			self.sdb.set_employee(eid, {the_body['name'], the_body['jobtitle'], the_body['basepay'], the_body['totalpay'], the_body['year'], the_body['agency']})
			output['id'] = eid
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def DELETE(self):
		output = {'result':'success'}
		try:
			self.sdb.delete_all_employees()
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

class EmployeeKeyController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self, mid):
		output = {'result':'success'}
		eid = int(eid)
		try:
			data = self.sdb.get_employee(eid)
			if data is None:
				raise KeyError
			output['id'] = templist[0]
			output['name'] = templist[1]
			output['jobtitle'] = templist[2]
			output['basepay'] = templist[3]
			output['totalpay'] = templist[4]
			output['year'] = templist[5]
			output['agency'] = templist[6]
		except KeyError as ex: 
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT(self, mid):
		output = {'result':'success'}
		eid = int(eid)
		the_body = cherrypy.request.body.read().decode()
		try:
			the_body = json.loads(the_body)
			self.sdb.set_employee(eid, {the_body['name'], the_body['jobtitle'], the_body['basepay'], the_body['totalpay'], the_body['year'], the_body['agency']})
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def DELETE(self, mid):
		output = {'result':'success'}
		eid = int(eid)
		try:
			self.sdb.delete_employee(eid)
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

class JobController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self):
		output = {'result':'success'}
		ldict = []
		try:
			jobtitles = self.sdb.get_jobs()
			for title in jobtitles:
				templist = self.sdb.get_job(title)
				tempdict = {}
				tempdict['title'] = title
				tempdict['ids'] = templist[1]
				ldict.append(tempdict)
			output['jobs'] = ldict
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

""" UNSURE ABOUT THIS ONE TOO """
	def POST(self):
		output = {'result':'success'}
		the_body = cherrypy.request.body.read().decode()
		jobl = []
		try:
			the_body = json.loads(the_body)
			jobtitles = self.sdb.get_jobs()
			for title in jobtitles:
				jobl.append(int(title))
			jobtitle = the_body['jobtitle']
			self.sdb.set_user(jobtitle, the_body['ids'])
			output['jobtitle'] = jobtitle
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

class JobKeyController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self, jobtitle):
		output = {'result':'success'}
		try:
			data = self.sdb.get_job(jobtitle)
			if data is None:
				raise KeyError
			output['jobtitle'] = data[0]
			output['ids'] = data[1]
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
""" DO WE NEED THIS???? """
	"""def PUT(self, jobtitle):
		output = {'result':'success'}
		the_body = cherrypy.request.body.read().decode()
		try:
			the_body = json.loads(the_body)
			self.sdb.set_user(uid, the_body['gender'], the_body['age'], the_body['occupation'], the_body['zipcode'])
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)"""

class SalaryController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self):
		output = {'result':'success'}
		try:
			bestsalary = self.sdb.get_best_salary_job()
			output['bestsalaryjob'] = bestsalary[0]
			output['bestsalaryamt'] = bestsalary[1]
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

class SalaryKeyController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self, uid):
		output = {'result':'success'}
		uid = int(uid)
		try:
			salary = self.sdb.get_average_totalpay()
			output['jobtitle'] = salary[0]
			output['salary'] = salary[1]
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

def start_service():
	sdb = _salaries_database()

	sdb.load_employees('Salaries.csv')
	sdb.load_jobs('Salaries.csv')

	employeeController = EmployeeController(sdb=sdb)
	employeeKeyController = EmployeeKeyController(sdb=sdb)
	jobController = JobController(sdb=sdb)
	jobKeyController = JobKeyController(sdb=sdb)
	salaryController = SalaryController(sdb=sdb)
	salaryKeyController = SalaryKeyController(sdb=sdb)

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	dispatcher.connect('employees_get', '/employees/', controller=employeeController, action='GET', conditions=dict(method=['GET']))
	
	dispatcher.connect('employees_get_key', '/employees/:eid', controller=employeeKeyController, action='GET', conditions=dict(method=['GET']))
	
	dispatcher.connect('employees_post', '/employees/', controller=employeeController, action='POST', conditions=dict(method=['POST']))

	dispatcher.connect('employees_put_key', '/employee/:eid', controller=employeeKeyController, action='PUT', conditions=dict(method=['PUT']))
	
	dispatcher.connect('employees_delete', '/employees/', controller=employeeController, action='DELETE', conditions=dict(method=['DELETE']))

	dispatcher.connect('employees_delete_key', '/employee/:eid', controller=employeeKeyController, action='DELETE', conditions=dict(method=['DELETE']))

	dispatcher.connect('jobs_get', '/jobs/', controller=jobController, action='GET', conditions=dict(method=['GET']))

	dispatcher.connect('jobs_post', '/jobs/', controller=jobController, action='POST', conditions=dict(method=['POST']))

	dispatcher.connect('jobs_get_key', '/jobs/:jobtitle', controller=jobKeyController, action='GET', conditions=dict(method=['GET']))

	dispatcher.connect('jobs_put_key', '/jobs/:jobtitle', controller=jobKeyController, action='PUT', conditions=dict(method=['PUT']))

	dispatcher.connect('salaries_get', '/salaries/', controller=salaryController, action='GET', conditions=dict(method=['GET']))

	dispatcher.connect('salaries_get_key', '/salaries/:jobtitle', controller=salaryKeyController, action='GET', conditions=dict(method=['GET']))

	conf = {
		'global': {
			'server.socket_host': 'student04.cse.nd.edu',
			'server.socket_port': 51016
		},
		'/': {'request.dispatch': dispatcher}
	}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()

