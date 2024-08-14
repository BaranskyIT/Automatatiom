import pytest
import requests
from lesson9.Pages.DataBase import DataBase
from lesson9.Pages.Employee import Employer

# URL и параметры подключения
X_client_URL = "http://example.com"
DATABASE_URL = "postgresql+psycopg2://user:password@localhost/testdb"

@pytest.mark.usefixtures("get_valid_token", "test_employee")
def test_create_employee(get_valid_token, db):
    token = get_valid_token
    headers = {'Authorization': f'Bearer {token}'}
    db_instance = DataBase(DATABASE_URL)
    db_instance.connect()
    
    employer = Employer(db_instance)
    
    new_employee = {
        "first_name": "New",
        "last_name": "Employee",
        "middle_name": "Middle",
        "phone": "0987654321",
        "email": "new.employee@example.com",
        "avatar_url": "http://example.com/new_avatar.jpg",
        "company_id": 1
    }
    
    employer.add_new(new_employee)
    emp_id = db_instance.get_employer_id(new_employee['email'])
    
    assert emp_id is not None
    db_instance.close()

@pytest.mark.usefixtures("get_valid_token", "test_employee")
def test_get_employee(get_valid_token, db):
    token = get_valid_token
    headers = {'Authorization': f'Bearer {token}'}
    db_instance = DataBase(DATABASE_URL)
    db_instance.connect()
    
    employer = Employer(db_instance)
    emp_id = db_instance.get_employer_id("test.user@example.com")
    
    employee_info = employer.get_info(emp_id)
    
    assert employee_info['email'] == "test.user@example.com"
    db_instance.close()

@pytest.mark.usefixtures("get_valid_token", "test_employee")
def test_update_employee(get_valid_token, db):
    db_instance = DataBase(DATABASE_URL)
    db_instance.connect()
    
    employer = Employer(db_instance)
    emp_id = db_instance.get_employer_id("test.user@example.com")
    
    updated_info = {
        "first_name": "Updated",
        "last_name": "User",
        "middle_name": "NewMiddle",
        "phone": "1112223333",
        "email": "updated.user@example.com",
        "avatar_url": "http://example.com/updated_avatar.jpg"
    }
    
    employer.change_info(emp_id, updated_info)
    
    employee_info = employer.get_info(emp_id)
    
    assert employee_info['first_name'] == "Updated"
    assert employee_info['email'] == "updated.user@example.com"
    db_instance.close()

@pytest.mark.usefixtures("get_valid_token", "test_employee")
def test_soft_delete_employee(get_valid_token, db):
    db_instance = DataBase(DATABASE_URL)
    db_instance.connect()
    
    employer = Employer(db_instance)
    emp_id = db_instance.get_employer_id("test.user@example.com")
    
    db_instance.delete_employer(emp_id)
    
    employee_info = employer.get_info(emp_id)
    
    assert employee_info is None
    db_instance.close()