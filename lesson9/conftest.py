import requests

class Company:
    """
    Класс для работы с информацией о компании.
    """

    def __init__(self, url: str) -> None:
        """
        Конструктор класса Company.

        :param url: URL для доступа к API компании.
        """
        self.url = url

    def get_id_company(self) -> int:
        """
        Получает ID компании с сервера.

        :return: ID последней компании в списке.
        """
        response = requests.get(self.url + '/company')
        response.raise_for_status()  # Добавлено для обработки ошибок HTTP
        return response.json()[-1]['id']
