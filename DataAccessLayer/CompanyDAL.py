from Model.company_model import CompanyModel
from DataAccessLayer.Connection import Connection


class CrudCompany:
    connection = Connection()

    def select_company_by_name(self, company: CompanyModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,name FROM companies WHERE name = ?"
        parameter = (company.CompanyName,)
        cursor.execute(query, parameter)
        company_info = cursor.fetchall()
        cursor.close()
        if not company_info:
            return None
        else:
            company_info_dictionary = {
                "id": company_info[0][0],
                "name": company_info[0][1]
            }
            return company_info_dictionary

    def select_company_by_id(self, company: CompanyModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,name FROM companies WHERE id = ?"
        parameter = (company.CompanyId,)
        cursor.execute(query, parameter)
        company_info = cursor.fetchall()
        cursor.close()
        if not company_info:
            return None
        else:
            company_info_dictionary = {
                "id": company_info[0][0],
                "name": company_info[0][1]
            }
            return company_info_dictionary

    def insert_company(self, company: CompanyModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO companies (name) VALUES (?)"
        parameter = (company.CompanyName,)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False

