from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class DataBase:

    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None
    
    def connect(self):
        self.session = self.Session()
    
    def close(self):
        if self.session:
            self.session.close()
    
    def execute_query(self, query, params=None):
        try:
            result = self.session.execute(text(query), params)
            self.session.commit()
            return result.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.session.rollback()
            self.close()

    def create_company(self, company_data):
        query = "INSERT INTO company (id, name) VALUES (:id, :name)"
        self.execute_query(query, company_data)

    def delete_company(self, company_id):
        query = "DELETE FROM company WHERE id = :id"
        self.execute_query(query, {'id': company_id})

    def last_company_id(self):
        query = "SELECT MAX(id) AS last_id FROM company"
        result = self.execute_query(query)
        return result[0]['last_id'] if result else None

    def get_list_employer(self, company_id):
        query = "SELECT * FROM employer WHERE company_id = :company_id"
        return self.execute_query(query, {'company_id': company_id})

    def create_employer(self, employer_data):
        query = """
            INSERT INTO employer (first_name, last_name, middle_name, phone, email, avatar_url, company_id) 
            VALUES (:first_name, :last_name, :middle_name, :phone, :email, :avatar_url, :company_id)
        """
        self.execute_query(query, employer_data)

    def get_employer_id(self, email):
        query = "SELECT id FROM employer WHERE email = :email"
        result = self.execute_query(query, {'email': email})
        return result[0]['id'] if result else None

    def update_employer_info(self, employer_id, update_data):
        query = """
            UPDATE employer 
            SET first_name = :first_name, last_name = :last_name, middle_name = :middle_name, 
                phone = :phone, email = :email, avatar_url = :avatar_url 
            WHERE id = :id
        """
        update_data['id'] = employer_id
        self.execute_query(query, update_data)

    def delete_employer(self, employer_id):
        query = "DELETE FROM employer WHERE id = :id"
        self.execute_query(query, {'id': employer_id})