import requests

class ApiEmployee:
    """
    Класс для работы с API сотрудников.
    """

    def __init__(self, url: str) -> None:
        """
        Конструктор класса ApiEmployee.

        :param url: URL для доступа к API сотрудников.
        """
        self.url = url

    def auth2(self, login: str = "leonardo", password: str = "leads") -> str:
        """
        Авторизуется в API и получает токен.

        :param login: Логин пользователя.
        :param password: Пароль пользователя.
        :return: Токен пользователя.
        """
        body = {
            "username": login,
            "password": password
        }
        response = requests.post(self.url + '/auth/login', json=body)
        response.raise_for_status()  # Добавлено для обработки ошибок HTTP
        return response.json()["userToken"]

    def get_list_employee2(self, params: str = None) -> requests.Response:
        """
        Получает список сотрудников компании.

        :param params: Параметры запроса.
        :return: Ответ от сервера.
        """
        response = requests.get(self.url + '/employee' + (params if params else ''))
        response.raise_for_status()  # Добавлено для обработки ошибок HTTP
        return response

    def add_new_employee2(self, body: dict) -> requests.Response:
        """
        Добавляет нового сотрудника через API.

        :param body: Данные нового сотрудника.
        :return: Ответ от сервера.
        """
        headers = {'x-client-token': self.auth2()}
        response = requests.post(self.url + '/employee/', headers=headers, json=body)
        response.raise_for_status()  # Добавлено для обработки ошибок HTTP
        return response

    def get_new_employee2(self, id: int) -> requests.Response:
        """
        Получает данные сотрудника по ID.

        :param id: ID сотрудника.
        :return: Ответ от сервера.
        """
        response = requests.get(self.url + '/employee/' + str(id))
        response.raise_for_status()  # Добавлено для обработки ошибок HTTP
        return response

    def change_new_employee2(self, id: int, new_body: dict) -> requests.Response:
        """
        Изменяет данные сотрудника.

        :param id: ID сотрудника.
        :param new_body: Новые данные сотрудника.
        :return: Ответ от сервера.
        """
        headers = {'x-client-token': self.auth2()}
        response = requests.patch(self.url + '/employee/' + str(id), headers=headers, json=new_body)
        response.raise_for_status()  # Добавлено для обработки ошибок HTTP
        return response
