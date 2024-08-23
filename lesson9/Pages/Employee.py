import requests


class ApiEmployee:

    def __init__(self, url) -> None:
        self.url = url

# Авторизация
    def auth2(self, login="leonardo", password="leads"):
        body = {
          "username": login,
          "password": password
        }
        response = requests.post(self.url + '/auth/login', json=body)
        return response.json()["userToken"]

# Получить список сотрудников компании
    def get_list_employee2(self, params=None):
        response = requests.get(self.url + '/employee' + params)
        return response

# Добавить нового сотрудника
    def add_new_employee2(self, body):
        headers = {'x-client-token': self.auth2()}
        response = requests.post(self.url + '/employee/', headers=headers, json=body)
        return response

# Получить сотрудника по id
    def get_new_employee2(self, id):
        response = requests.get(self.url + '/employee/' + str(id))
        return response

# Изменить данные о новом сотруднике
    def change_new_employee2(self, id, new_body):
        headers = {'x-client-token': self.auth2()}
        response = requests.patch(self.url + '/employee/' + str(id), headers=headers, json=new_body)
        return response