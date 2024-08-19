# from lesson8.Pages.Employee import Employer, Company
# from lesson8.constants import X_client_URL

# employer = Employer()
# company = Company()

# def test_authorization(get_token):
#     token = get_token
#     assert token is not None
#     assert isinstance(token, str)

# def test_getcompany_id():
#     company_id = company.last_company_id()
#     assert company_id is not None
#     assert str(company_id).isdigit()

# def test_add_employeer(get_token):
#     token = str(get_token)
#     com_id = company.last_company_id()
#     body_employer = {
#         "id": 0,
#         "firstName": "Pavel",
#         "lastName": "Mamaev",
#         "middleName": "string",
#         "companyId": com_id,
#         "email": "pm@mail.com",
#         "url": "string",
#         "phone": "string",
#         "birthdate": "2024-08-12T15:27:44.161Z",
#         "isActive": 'true'
#     }
#     response = employer.add_new(token, body_employer)
#     print(f"Ответ сервера: {response}") 

#     assert 'id' in response, f"Ожидался ключ 'id' в ответе, но получили {response}"
#     new_employer_id = response['id']


# def test_add_empl_without_body(get_token):
#     token = str(get_token)
#     com_id = company.last_company_id()
#     body_employer = {}
#     new_employer = employer.add_new(token, body_employer)
    
#     assert new_employer['message'] in ['Unauthorized', 'Internal server error'], \
#         f"Неожиданное сообщение: {new_employer.get('message')}"

# def test_get_employer():
#     com_id = company.last_company_id()
#     list_employers = employer.get_list(com_id)
#     assert isinstance(list_employers, list)

# def test_get_list_employers_missing_company_id():
#     try:
#         employer.get_list()
#     except TypeError as e:
#         assert str(
#         e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

# def test_get_list_employers_invalid_company_id():
#     try:
#         employer.get_list()
#     except TypeError as e:
#         assert str(
#         e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

# def test_get_info_new_employers_missing_employer_id():
#     try: 
#         employer.get_info()
#     except TypeError as e: 
#         assert str(
#             e) == "Employer.get_info() missing 1 required positional argument: 'employee_id'"
        

# def test_change_employer_info(get_token):
#     token = str(get_token)
#     com_id = company.last_company_id()
#     body_employer = {
#         "id": 0,
#         "firstName": "Pavel",
#         "lastName": "Mamaev",
#         "middleName": "string",
#         "companyId": com_id,
#         "email": "pm@mail.com",
#         "url": "string",
#         "phone": "string",
#         "birthdate": "2024-08-12T15:27:44.161Z",
#         "isActive": 'true'
#     }
#     just_employer = employer.add_new(token, body_employer)
#     print(just_employer)  # Отладка: проверьте структуру ответа

#     # Проверяем, что ключ 'id' есть в ответе
#     assert 'id' f"Ожидался ключ 'id' в ответе, но получили {just_employer}"
#     id = just_employer['id']

#     body_change_employer = {
#         "firstName": "Pavel",
#         "lastName": "Mamaev",
#         "email": "pavmam@gmail.com",
#         "phone": "89186000550",
#         "isActive": 'true'
#     }
#     employer_changed = employer.change_info(token, id, body_change_employer)
#     assert employer_changed.status_code == 200
#     assert employer_changed.json()['email'] == body_change_employer.get('email')

# def test_employers_missing_id_and_token():
#     try:
#         employer.change_info()
#     except TypeError as e:
#         assert str(e) == "Employer.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"

# from lesson8.Pages.Employee import WorkersApi

# api = WorkersApi()

# def test_add_new_employee():
#     company = api.create_company("Luna Inc.", "Управление солнечными батареями")
#     companyId = company["id"]

#     employees_before = api.get_employees_list(companyId)
#     len_before = len(employees_before)

#     new_employee = api.create_employee("Мария", "Светлова", "Андреевна", companyId, "maria.bright@mail.com", "89001234567", "1994-04-12")
#     emp_id = new_employee["id"]

#     employees_after = api.get_employees_list(companyId)
#     len_after = len(employees_after)

#     assert len_after - len_before == 1
#     assert any(emp["id"] == emp_id for emp in employees_after)

# def test_patch_employee():
#     company = api.create_company("Космический Туризм", "Путешествия за пределами Земли")
#     companyId = company["id"]

#     new_employee = api.create_employee("Александр", "Космонавт", "Сергеевич", companyId, "alex.kosmonav@mail.com", "89080003456", "1992-09-21")
#     emp_id = new_employee["id"]

#     edited = api.edit_employee(emp_id, "Морозов", "updated.email@mail.com", "updated-phone", False)
    
#     assert edited["email"] == "updated.email@mail.com"
#     assert edited["isActive"] == False

# def test_delete_employee():
#     company = api.create_company("Лазурные Берега", "Туристическая компания")
#     companyId = company["id"]

#     new_employee = api.create_employee("Татьяна", "Синюкова", "Петровна", companyId, "tatiana.sinyuk@mail.com", "89112345678", "1988-02-20")
#     emp_id = new_employee["id"]

#     del_emp = api.delete_employee(emp_id)
#     assert del_emp is not None
import pytest
from lesson8.Pages.Employee import WorkersApi

api = WorkersApi()

def test_add_new_employee():
    company = api.create_company("Luna Inc.", "Управление солнечными батареями")
    companyId = company["id"]

    employees_before = api.get_employees_list(companyId)
    len_before = len(employees_before)

    new_employee = api.create_employee("Мария", "Светлова", "Андреевна", companyId, "maria.bright@mail.com", "89001234567", "1994-04-12")
    emp_id = new_employee["id"]

    employees_after = api.get_employees_list(companyId)
    len_after = len(employees_after)

    assert len_after - len_before == 1
    assert any(emp["id"] == emp_id for emp in employees_after)

def test_get_employee():
    company = api.create_company("Титановая руда", "Добыча редкоземельных металлов")
    companyId = company["id"]

    new_employee = api.create_employee("Иван", "Долгорукий", "Иванович", companyId, "ivan.dolg@mail.com", "89090001234", "1985-07-15")
    emp_id = new_employee["id"]

    fetched_employee = api.get_employee(emp_id)

    assert fetched_employee["id"] == emp_id
    assert fetched_employee["firstName"] == "Иван"
    assert fetched_employee["lastName"] == "Долгорукий"

def test_patch_employee():
    company = api.create_company("Космический Туризм", "Путешествия за пределами Земли")
    companyId = company["id"]

    new_employee = api.create_employee("Александр", "Космонавт", "Сергеевич", companyId, "alex.kosmonav@mail.com", "89080003456", "1992-09-21")
    emp_id = new_employee["id"]

    edited = api.edit_employee(emp_id, "Морозов", "updated.email@mail.com", "updated-phone", False)
    
    assert edited["email"] == "updated.email@mail.com"
    assert edited["isActive"] == False

def test_delete_employee():
    company = api.create_company("Лазурные Берега", "Туристическая компания")
    companyId = company["id"]

    new_employee = api.create_employee("Татьяна", "Синюкова", "Петровна", companyId, "tatiana.sinyuk@mail.com", "89112345678", "1988-02-20")
    emp_id = new_employee["id"]

    del_emp = api.delete_employee(emp_id)
    assert del_emp is not None

def test_required_fields():
    company = api.create_company("Золотая Арена", "Комплексный подход")

    companyId = company["id"]

    with pytest.raises(ValueError) as excinfo:
        api.create_employee("", "Примаков", "Александрович", companyId, "primakov.alex@mail.com", "89876543210", "1980-05-12")
    assert "Firstname, Lastname and Email are required fields." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        api.create_employee("Анна", "", "Викторовна", companyId, "anna.vik@mail.com", "89991234567", "1995-03-10")
    assert "Firstname, Lastname and Email are required fields." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        api.create_employee("Лена", "Петрова", "", companyId, "", "89987654321", "1990-12-01")
    assert "Firstname, Lastname and Email are required fields." in str(excinfo.value)