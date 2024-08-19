import requests
from lesson8.constants import X_client_URL

class WorkersApi:
    def __init__(self, url=X_client_URL):
        self.url = url
        self.token = self.get_token()

    def get_token(self, user='leonardo', password='leads'):
        creds = {'username': user, 'password': password}
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        
        print(f"Response Status Code: {resp.status_code}")
        print(f"Response JSON: {resp.json()}")

        if resp.status_code in [200, 201]:
            try:
                return resp.json()['userToken']
            except KeyError:
                print(f"Error: 'userToken' not found in response: {resp.json()}")
                raise
        else:
            print(f"Error: Unexpected response status {resp.status_code}")
            raise Exception(f"Failed to get token: {resp.json()}")

    def create_company(self, name, description=""):
        company = {"name": name, "description": description}
        headers = {"x-client-token": self.token}
        resp = requests.post(f"{self.url}/company", json=company, headers=headers)
        return resp.json()

    def get_company(self, id):
        resp = requests.get(f"{self.url}/company/{id}")
        return resp.json()

    def get_employee(self, id):
        headers = {"x-client-token": self.token}
        resp = requests.get(f"{self.url}/employee/{id}", headers=headers)
        return resp.json()

    def get_employees_list(self, companyId):
        resp = requests.get(f"{self.url}/employee", params={'company': companyId})
        return resp.json()

    def create_employee(self, firstName, lastName, middleName, companyId, email, phone, birthdate):
        if not firstName or not lastName or not email:
            raise ValueError("Firstname, Lastname and Email are required fields.")
        
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": True
        }
        headers = {"x-client-token": self.token}
        resp = requests.post(f"{self.url}/employee", json=employee, headers=headers)
        return resp.json()

    def edit_employee(self, id, lastName, email, phone, isActive):
        employee = {
            "lastName": lastName,
            "email": email,
            "phone": phone,
            "isActive": isActive
        }
        headers = {"x-client-token": self.token}
        resp = requests.patch(f"{self.url}/employee/{id}", json=employee, headers=headers)
        return resp.json()

    def delete_employee(self, id):
        headers = {"x-client-token": self.token}
        resp = requests.delete(f"{self.url}/employee/{id}", headers=headers)
        return resp.json()