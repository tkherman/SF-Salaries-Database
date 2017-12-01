import cherrypy
import re
import json
import urllib
from _salaries_database import _salaries_database

class EmployeeController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	# Get all employees
	def GET(self):
		output = {'result':'success'}
		ldict = []
		try:
			# Append each employee info to list
			employee_ids = self.sdb.get_employees()
			for eid in employee_ids:
				ldict.append(self.sdb.get_employee(eid))
			output['employees'] = ldict
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output)

	def POST(self):
		output = {'result':'success'}
		the_body = cherrypy.request.body.read().decode()
		the_body = json.loads(the_body)

		# Ensure all fields are present
		try:
			the_body["Id"] = float(the_body["Id"])
			the_body["EmployeeName"]
			the_body["JobTitle"]
			the_body["BasePay"] = float(the_body["BasePay"])
			the_body["TotalPay"] = float(the_body["TotalPay"])
			the_body["Year"] = float(the_body["Year"])
			the_body["Agency"]
			self.sdb.set_employee(the_body["Id"], the_body)
		except KeyError:
			output['result'] = "failure"
			output['message'] = "input missing entries"


		return json.dumps(output)

	def DELETE(self):
		output = {'result':'success'}
		self.sdb.delete_all_employees()
		return json.dumps(output)

class EmployeeKeyController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self, eid):
		output = {'result':'success'}
		eid = int(eid)
		try:
			data = self.sdb.get_employee(eid)
			# Check that data is valid
			if data is None:
				raise KeyError
			output.update(data)
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT(self, eid):
		output = {'result':'success'}
		eid = int(eid)
		the_body = cherrypy.request.body.read().decode()
		the_body = json.loads(the_body)

		# Ensure all fields are present
		try:
			the_body["Id"] = float(the_body["Id"])
			the_body["EmployeeName"]
			the_body["JobTitle"]
			the_body["BasePay"] = float(the_body["BasePay"])
			the_body["TotalPay"] = float(the_body["TotalPay"])
			the_body["Year"] = float(the_body["Year"])
			the_body["Agency"]
			self.sdb.set_employee(the_body["Id"], the_body)
		except KeyError:
			output['result'] = 'failure'
			output['message'] = 'input missing entries'

		return json.dumps(output)

	def DELETE(self, eid):
		output = {'result':'success'}
		eid = int(eid)

		# Prevent cases where eid doesn't exist in database
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

		# Providie a list of job titles
		output['JobTitles'] = list(self.sdb.get_jobs())

		return json.dumps(output)


class JobKeyController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

<<<<<<< HEAD
	def GET(self, jobtitle):
		output = {'result':'success'}
		jobtitle = urllib.parse.unquote(jobtitle)
=======
    def GET(self, jobtitle):
        output = {'result':'success'}
        # decode job title from url
        jobtitle = urllib.parse.unquote(jobtitle)
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

		try:
			data = self.sdb.get_job(jobtitle)
			if data is None:
				raise KeyError
			output['JobTitle'] = jobtitle
			output['Ids'] = data
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = "invalid job title"

		return json.dumps(output)

<<<<<<< HEAD
	def DELETE(self, jobtitle):
		output = {'result': 'success'}
		jobtitle = urllib.parse.unquote(jobtitle)
=======
    def DELETE(self, jobtitle):
        output = {'result': 'success'}
        # decode job title from url
        jobtitle = urllib.parse.unquote(jobtitle)
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

		try:
			Ids = self.sdb.get_job(jobtitle)
			if Ids == None:
				raise KeyError
			for Id in Ids:
				self.sdb.delete_employee(Id)
		except KeyError:
			output['result'] = 'failure'

		return json.dumps(output)


class SalaryController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self):
		output = {'result':'success'}

		bestsalary = self.sdb.get_best_salary_job()
		output['BestSalary'] = bestsalary['BestSalary']
		output['BestJob'] = bestsalary['BestJob']

		return json.dumps(output)

class SalaryKeyController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

	def GET(self, jobtitle):
		output = {'result':'success'}
		jobtitle = urllib.parse.unquote(jobtitle)

<<<<<<< HEAD
		# Get salary while catching exception for if jobtitle is not valid
		try:
			salary = self.sdb.get_average_totalpay()
			output['JobTitle'] = jobtitle
			output['AverageSalary'] = salary
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = "JobTitle is not valid"
=======
        # Get salary while catching exception for if jobtitle is not valid
        try:
            salary = self.sdb.get_average_totalpay(jobtitle)
            output['JobTitle'] = jobtitle
            output['AverageSalary'] = salary
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = "JobTitle is not valid"
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

		return json.dumps(output)

class ResetController(object):
	def __init__(self, sdb = None):
		self.sdb = sdb

<<<<<<< HEAD
	def PUT(self):
		output = {'result': 'success'}
		self.sdb.delete_all_employees()
		self.sdb.load_employees("Salaries.csv")
		self.sdb.load_jobs("Salaries.csv")
=======
    def PUT(self):
        output = {'result': 'success'}
        # delete_all_employees also wipe the jobs database
        self.sdb.delete_all_employees()
        # reload the two dictionaries
        self.sdb.load_employees("Salaries.csv")
        self.sdb.load_jobs("Salaries.csv")
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

		return json.dumps(output)


def start_service():
<<<<<<< HEAD
	sdb = _salaries_database()
=======
    # Create an instance of database
    sdb = _salaries_database()
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

	sdb.load_employees('Salaries.csv')
	sdb.load_jobs('Salaries.csv')

<<<<<<< HEAD
	employeeController = EmployeeController(sdb=sdb)
	employeeKeyController = EmployeeKeyController(sdb=sdb)
	jobController = JobController(sdb=sdb)
	jobKeyController = JobKeyController(sdb=sdb)
	salaryController = SalaryController(sdb=sdb)
	salaryKeyController = SalaryKeyController(sdb=sdb)
	resetController = ResetController(sdb=sdb)
=======
    # Instantiate controllers
    employeeController = EmployeeController(sdb=sdb)
    employeeKeyController = EmployeeKeyController(sdb=sdb)
    jobController = JobController(sdb=sdb)
    jobKeyController = JobKeyController(sdb=sdb)
    salaryController = SalaryController(sdb=sdb)
    salaryKeyController = SalaryKeyController(sdb=sdb)
    resetController = ResetController(sdb=sdb)
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

	dispatcher = cherrypy.dispatch.RoutesDispatcher()

<<<<<<< HEAD
	dispatcher.connect('employees_get', '/employees/', controller=employeeController, action='GET', conditions=dict(method=['GET']))
=======
    # Connect controllers
    dispatcher.connect('employees_get', '/employees/', controller=employeeController, action='GET', conditions=dict(method=['GET']))
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

	dispatcher.connect('employees_get_key', '/employees/:eid', controller=employeeKeyController, action='GET', conditions=dict(method=['GET']))

	dispatcher.connect('employees_post', '/employees/', controller=employeeController, action='POST', conditions=dict(method=['POST']))

	dispatcher.connect('employees_put_key', '/employees/:eid', controller=employeeKeyController, action='PUT', conditions=dict(method=['PUT']))

	dispatcher.connect('employees_delete', '/employees/', controller=employeeController, action='DELETE', conditions=dict(method=['DELETE']))

	dispatcher.connect('employees_delete_key', '/employees/:eid', controller=employeeKeyController, action='DELETE', conditions=dict(method=['DELETE']))

	dispatcher.connect('jobs_get', '/jobs/', controller=jobController, action='GET', conditions=dict(method=['GET']))

<<<<<<< HEAD
	dispatcher.connect('jobs_post', '/jobs/', controller=jobController, action='POST', conditions=dict(method=['POST']))

	dispatcher.connect('jobs_get_key', '/jobs/:jobtitle', controller=jobKeyController, action='GET', conditions=dict(method=['GET']))

	dispatcher.connect('jobs_put_key', '/jobs/:jobtitle', controller=jobKeyController, action='PUT', conditions=dict(method=['PUT']))
=======
    dispatcher.connect('jobs_get_key', '/jobs/:jobtitle', controller=jobKeyController, action='GET', conditions=dict(method=['GET']))

    dispatcher.connect('jobs_delete_key', '/jobs/:jobtitle', controller=jobKeyController, action='DELETE', conditions=dict(method=['DELETE']))
>>>>>>> f7162aa7367064101fddb743348057f967db9bdc

	dispatcher.connect('salaries_get', '/salaries/', controller=salaryController, action='GET', conditions=dict(method=['GET']))

	dispatcher.connect('salaries_get_key', '/salaries/:jobtitle', controller=salaryKeyController, action='GET', conditions=dict(method=['GET']))

	dispatcher.connect('reset', '/reset/', controller=resetController, action='PUT', conditions=dict(method=['PUT']))

	conf = {
		'global': {
				'server.socket_host': 'student04.cse.nd.edu',
				'server.socket_port': 51076
		},
		'/': {'request.dispatch': dispatcher}
	}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

if __name__ == '__main__':
	start_service()
