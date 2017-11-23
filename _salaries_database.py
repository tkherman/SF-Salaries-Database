import sys

class _salaries_database:

    def __init__(self):
        self.employees = dict()
        self.jobs = dict()

    """
        Employees
            - store employees information in a dictionary
            - key = id
            - value = a dictionary of employee information with keys:
              Id, EmployeeName, JobTitle, BasePay, TotalPay, Year, Agency
    """
    def load_employees(self, salaries_file):
        with open(salaries_file, "r") as f:
            # Get column headers
            columns = next(f).split(",")

            for line in f:
                employee = line.rstrip().split(",")

                # Combine fields that begins with " and seaparted by ,
                if employee[1][0] == '"':
                    index = 2
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[1:index+1] = ["".join(employee[1:index+1])]

                if employee[2][0] == '"':
                    index = 3
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[2:index+1] = ["".join(employee[2:index+1])]

                info =  dict()

                for i in range(len(columns)):
                    if employee[i].replace(".", "").isdigit():
                        info[columns[i]] = float(employee[i])
                    else:
                        info[columns[i]] = employee[i]

                del info['OvertimePay']
                del info['OtherPay']
                del info['Benefits']
                del info['TotalPayBenefits']
                del info['Notes']
                del info['Status\n']

                self.employees[info['Id']] = info

    def get_employee(self, eid):
        return self.employees.get(eid)

    def get_employees(self):
        return self.employees.keys()

    def set_employee(self, eid, data):
        # If employee exist under eid, remove the eid from its job's list
        if self.employees.get(eid):
            current_employee = self.employees[eid]
            self.jobs[current_employee['JobTitle']].remove(current_employee['Id'])

        self.employees[eid] = data

        # Update self.jobs with new employee
        try:
            self.jobs[data['JobTitle']].append(data['Id'])
        except KeyError:
            self.jobs[data['JobTitle']] = [data['Id']]


    def delete_employee(self, eid):
        del self.employees[eid]

    def delete_all_employees(self):
        self.employees.clear()

    """
        JOBS
            - store employee Ids of different jobs
            - store as dictionary
            - key = JobTitle
            - value = list of Ids
    """
    def load_jobs(self, salaries_file):
        with open(salaries_file, "r") as f:
            # Get column headers
            columns = next(f).split(",")

            for line in f:
                employee = line.rstrip().split(",")

                # Combine fields that begins with " and seaparted by ,
                if employee[1][0] == '"':
                    index = 2
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[1:index+1] = ["".join(employee[1:index+1])]

                if employee[2][0] == '"':
                    index = 3
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[2:index+1] = ["".join(employee[2:index+1])]

                try:
                    self.jobs[employee[2]].append(float(employee[0]))
                except KeyError:
                    self.jobs[employee[2]] = [float(employee[0])]

    def get_jobs(self):
        return self.jobs.keys()

    def get_job(self, JobTitle):
        return self.jobs[JobTitle]

"""
database = _salaries_database()
database.load_employees("Salaries.csv")
database.load_jobs("Salaries.csv")

print(database.get_job("CAPTAIN III (POLICE DEPARTMENT)"))

print(database.get_jobs())"""
