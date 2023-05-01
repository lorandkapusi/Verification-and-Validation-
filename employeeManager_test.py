from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager
import datetime

relation_manager = RelationsManager()
employee_manager = EmployeeManager(relation_manager)

#Check an employee’s salary who is not a team leader whose hire date is 10.10.1998 and his base salary is 1000$. Make sure the returned value is 3000$ (1000$ + 20 X 100$).
def test_employee_salary_not_team_leader():
    expedted_salary = 3000
    
    employee = Employee(id=7, first_name="Johnny", last_name="Bravo", base_salary=1000,
                  birth_date=datetime.date(1970, 1, 31), 
                  hire_date=datetime.date(1998, 10, 10))
    
    employee_salary = employee_manager.calculate_salary(employee)

    assert expedted_salary == employee_salary



def test_employee_salary_team_leader():
    
    expedted_salary = 3600
    
    employee = Employee(id=7, first_name="Julia", last_name="Doe", base_salary=2000,
                  birth_date=datetime.date(1970, 1, 31), 
                  hire_date=datetime.date(2008, 10, 10))
    
    relation_manager.teams.update({7:[1,2,3]})

    employee_salary = employee_manager.calculate_salary(employee) 

    assert expedted_salary == employee_salary



def test_calculate_salary_and_send_email(capsys):

    """ Make sure that when you calculate the salary and send an email notification,
    the respective email sender service is used with the correct information (name and message). 
    You can use the setup from the previous test for the employee.
    
    """

    employee = Employee(id=7, first_name="Julia", last_name="Doe", base_salary=2000,
                  birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(2008, 10, 10))
    
    relation_manager.teams.update({7:[1,2,3]})
    
    employee_manager.calculate_salary_and_send_email(employee)
   
    captured = capsys.readouterr()
    assert captured.out == "Julia Doe your salary: 3600 has been transferred to you."+'\n'
