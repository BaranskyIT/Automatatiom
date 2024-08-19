# import requests
# import json
# from lesson8.constants import X_client_URL

# path = '/employee/'

# class Company:
#     def __init__(self, url=X_client_URL):
#         self.url = url

#     def create(self, token: str,  body: json):
#         headers = {'x-clients-token': token}
#         response = requests.post(
#             self.url + '/company/', headers=headers, params=body)
#         return response.json()
    
#     def last_company_id(self):
#         active_params = {'active': 'true'}
#         responce = requests.get(
#             self.url + '/company/', params=active_params)
#         return responce.json()[-1]['id']
    
# class Employer:
#     def __init__(self, url=X_client_URL):
#         self.url = url

#     def get_list(self, company_id: int):
#         company = {'company': company_id}
#         response = requests.get(
#             self.url + '/employee', params=company)
#         return response.json()
    
#     def add_new(self, token: str, body: json):
#         headers = {'x-clients-token': token}
#         response = requests.post(
#             self.url + '/employee', headers=headers, json=body)
#         return response.json()
    
#     def get_info(self, employee_id: int):
#         response = requests.get(self.url + path + str(employee_id))
#         return response
    
#     def change_info(self, token: str, employee_id: int, body: json):
#         headers = {'x-clients-token': token}
#         response = requests.patch(self.url + path + str(employee_id), headers=headers, json=body)
#         return response

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