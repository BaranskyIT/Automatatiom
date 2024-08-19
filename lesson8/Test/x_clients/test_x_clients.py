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