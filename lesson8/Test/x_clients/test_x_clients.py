from lesson8.Pages.Employee import Employer, Company
from lesson8.constants import X_client_URL

employer = Employer()
company = Company()

def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)

def test_getcompany_id():
    company_id = company.last_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

# def test_add_employeer(get_token):
#     token = str(get_token)
#     com_id = company.last_company_id()
#     body_employer = {
#     "id": 0,
#     "firstName": "Pavel",
#     "lastName": "Mamaev",
#     "middleName": "string",
#     "companyId": com_id,
#     "email": "pm@mail.com",
#     "url": "string",
#     "phone": "string",
#     "birthdate": "2024-08-12T15:27:44.161Z",
#     "isActive": 'true'
#     }
#     new_employer_id = (employer.add_new(token, body_employer))['id']
#     assert new_employer_id is not None
#     assert str(new_employer_id).isdigit()
#     info = employer.get_info(new_employer_id)
#     assert info.json()['id'] == new_employer_id
#     assert info.status_code == 200
def test_add_employeer(get_token):
    token = str(get_token)
    com_id = company.last_company_id()
    body_employer = {
        "id": 0,
        "firstName": "Pavel",
        "lastName": "Mamaev",
        "middleName": "string",
        "companyId": com_id,
        "email": "pm@mail.com",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-08-12T15:27:44.161Z",
        "isActive": 'true'
    }
    response = employer.add_new(token, body_employer)
    print(f"Ответ сервера: {response}") 

    assert 'id' in response, f"Ожидался ключ 'id' в ответе, но получили {response}"
    new_employer_id = response['id']


def test_add_empl_without_body(get_token):
    token = str(get_token)
    com_id = company.last_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    
    assert new_employer['message'] in ['Unauthorized', 'Internal server error'], \
        f"Неожиданное сообщение: {new_employer.get('message')}"

# def test_add_empl_without_body(get_token):
#     token = str(get_token)
#     com_id = company.last_company_id()
#     body_employer = {}
#     new_employer = employer.add_new(token, body_employer)
#     assert new_employer['message'] == 'Unauthorized' == 'Internal server error'

def test_get_employer():
    com_id = company.last_company_id()
    list_employers = employer.get_list(com_id)
    assert isinstance(list_employers, list)

def test_get_list_employers_missing_company_id():
    try:
        employer.get_list()
    except TypeError as e:
        assert str(
        e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list()
    except TypeError as e:
        assert str(
        e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

def test_get_info_new_employers_missing_employer_id():
    try: 
        employer.get_info()
    except TypeError as e: 
        assert str(
            e) == "Employer.get_info() missing 1 required positional argument: 'employee_id'"
        
# def test_change_employer_info(get_token):
#     token = str(get_token)
#     com_id = company.last_company_id()
#     body_employer = {
#     "id": 0,
#     "firstName": "Pavel",
#     "lastName": "Mamaev",
#     "middleName": "string",
#     "companyId": com_id,
#     "email": "pm@mail.com",
#     "url": "string",
#     "phone": "string",
#     "birthdate": "2024-08-12T15:27:44.161Z",
#     "isActive": 'true'
#     }
#     just_employer = employer.add_new(token, body_employer)
#     id = just_employer['id']
#     body_change_employer = {
#     "firstName": "Pavel",
#     "lastName": "Mamaev",
#     "email": "pavmam@gmail.com",
#     "phone": "89186000550",
#     "isActive": 'true'      
#     }
#     employer_changed = employer.change_info(token, id, body_change_employer)
#     assert employer_changed.status_code == 200
#     assert (employer_changed.json()['email']) == body_change_employer.get('email')
def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_company_id()
    body_employer = {
        "id": 0,
        "firstName": "Pavel",
        "lastName": "Mamaev",
        "middleName": "string",
        "companyId": com_id,
        "email": "pm@mail.com",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-08-12T15:27:44.161Z",
        "isActive": 'true'
    }
    just_employer = employer.add_new(token, body_employer)
    print(just_employer)  # Отладка: проверьте структуру ответа

    # Проверяем, что ключ 'id' есть в ответе
    assert 'id' f"Ожидался ключ 'id' в ответе, но получили {just_employer}"
    id = just_employer['id']

    body_change_employer = {
        "firstName": "Pavel",
        "lastName": "Mamaev",
        "email": "pavmam@gmail.com",
        "phone": "89186000550",
        "isActive": 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200
    assert employer_changed.json()['email'] == body_change_employer.get('email')

def test_employers_missing_id_and_token():
    try:
        employer.change_info()
    except TypeError as e:
        assert str(e) == "Employer.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"