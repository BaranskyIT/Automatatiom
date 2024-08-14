class Employer:
    
    def __init__(self, db_instance):
        self.db = db_instance
    
    def get_list(self, company_id):
        return self.db.get_list_employer(company_id)
    
    def add_new(self, employer_data):
        self.db.create_employer(employer_data)
    
    def get_info(self, employer_id):
        query = "SELECT * FROM employer WHERE id = :id"
        result = self.db.execute_query(query, {'id': employer_id})
        return result[0] if result else None
    
    def change_info(self, employer_id, update_data):
        self.db.update_employer_info(employer_id, update_data)