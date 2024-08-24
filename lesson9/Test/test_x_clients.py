import allure
from lesson9.Pages.Employee import ApiEmployee
from lesson9.conftest import Company
from lesson9.Pages.DataBase import DbEmployee

db = DbEmployee("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
company = Company("https://x-clients-be.onrender.com")

param_id = "?company=" + str(company.get_id_company())
company_id = company.get_id_company()
api = ApiEmployee("https://x-clients-be.onrender.com")

body = {
    "id": 1111100011,
    "firstName": "string",
    "lastName": "string",
    "middleName": "string",
    "companyId": company_id,
    "email": "string@bl.yu",
    "url": "string",
    "phone": "string",
    "birthdate": "2023-08-14T11:02:45.622Z",
    "isActive": "true"
}

@allure.title("Получить список сотрудников")
@allure.description("Проверяет соответствие количества сотрудников в API и базе данных")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.NORMAL)
def test_get_list_employee2():
    with allure.step("Получение списка сотрудников из API"):
        api_result = api.get_list_employee2(param_id).json()
    with allure.step("Получение списка сотрудников из базы данных"):
        db_result = db.get_list_employee(company_id)
    assert len(api_result) == len(db_result)

@allure.title("Добавить нового сотрудника")
@allure.description("Проверяет возможность добавления нового сотрудника и его появление в списке API")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_employee2():
    with allure.step("Получение списка сотрудников из базы данных до добавления"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Добавление нового сотрудника через API"):
        api.add_new_employee2(body)
    with allure.step("Получение списка сотрудников из API после добавления"):
        api_response = api.get_list_employee2(param_id).json()
    assert len(api_response) - len(db_result) == 1

@allure.title("Проверка нового сотрудника")
@allure.description("Проверяет, что новый сотрудник, добавленный через API, присутствует в базе данных")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_new_employee2():
    with allure.step("Получение нового сотрудника из API"):
        resp = api.get_list_employee2(param_id)
        api_new_employee = resp.json()[-1]['id']
    with allure.step("Получение нового сотрудника из базы данных"):
        db_new_employee = db.get_id_new_employee()
    assert api_new_employee == db_new_employee

@allure.title("Создание сотрудника")
@allure.description("Проверяет создание нового сотрудника и его корректное отображение в API")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_employee():
    with allure.step("Получение списка сотрудников из базы данных до создания"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Добавление нового сотрудника в базу данных"):
        db.add_new_employee("Гена", "Букин", "1234567890", True, company_id)
    with allure.step("Получение данных о новом сотруднике из API"):
        data_employee = api.get_new_employee2(db.get_id_new_employee()).json()
    assert data_employee["firstName"] == "Гена"
    assert data_employee["lastName"] == "Букин"
    assert data_employee["phone"] == "1234567890"
    assert data_employee["isActive"] is True
    assert data_employee["companyId"] == company_id
    id = db.get_id_new_employee()
    with allure.step("Удаление созданного сотрудника из базы данных"):
        db.delete(id)

@allure.title("Редактирование сотрудника")
@allure.description("Проверяет изменение данных сотрудника и их корректное отображение в API")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_employee():
    with allure.step("Добавление нового сотрудника для редактирования"):
        db.add_new_employee("Гена", "Букин", "1234567890", True, company_id)
    id = db.get_id_new_employee()
    with allure.step("Редактирование данных сотрудника"):
        db.edit_employee("Филипп", "Басков", "0987654321", True, id)
    with allure.step("Получение обновленных данных сотрудника из API"):
        data_employee = api.get_new_employee2(id).json()
    assert data_employee["firstName"] == "Филипп"
    assert data_employee["lastName"] == "Басков"
    assert data_employee["phone"] == "0987654321"
    assert data_employee["isActive"] is True
    assert data_employee["companyId"] == company_id
    with allure.step("Удаление отредактированного сотрудника из базы данных"):
        db.delete(id)
