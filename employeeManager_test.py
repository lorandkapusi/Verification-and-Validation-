import employee_manager
from relations_manager import RelationsManager
import datetime
from employee import Employee 


def test_team_leader():
    rm = RelationsManager()
    all_employees = rm.get_all_employees()
    john_doe = None
    for employee in all_employees:
        if employee.first_name == "John" and employee.last_name == "Doe" and employee.birth_date == datetime.date(1970, 1, 31):
            john_doe = employee
            break
    assert john_doe is not None, "Test failed, there is no employee named John Doe with birthdate 31.01.1970"
    assert rm.is_leader(john_doe), "Test failed, John Doe is not a team leader"


def test_john_doe_team_members():
    rm = RelationsManager()
    john_doe = rm.employee_list[0]
    team_members = rm.get_team_members(john_doe)
    expected_members = [2, 3]
    actual_members = [e.id for e in rm.employee_list if e.id in team_members]
    actual_names = [e.first_name + ' ' + e.last_name for e in rm.employee_list if e.id in team_members]
    expected_names = ['Myrta Torkelson', 'Jettie Lynch']
    assert actual_members == expected_members, f"Expected members: {expected_members}, Actual members: {actual_members}"
    assert actual_names == expected_names, f"Expected names: {expected_names}, Actual names: {actual_names}"

def test_tomas_andre_not_john_doe_team_member():
    rm = RelationsManager()
    john_doe = rm.employee_list[0]
    team_members = rm.get_team_members(john_doe)
    tomas = next((e for e in rm.employee_list if e.first_name == "Tomas"), None)
    assert tomas is not None, "Tomas Andre not found in employee list"
    assert tomas.id not in team_members, "Tomas Andre is a member of John Doe's team"
