from Model.drug_model import DrugModel
from DataAccessLayer.Connection import Connection


class CrudDrug:
    connection = Connection()

    def select_drug_by_name(self, drug: DrugModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,category_id, product_name, price, company_id, description, count FROM drugs WHERE product_name = ?"
        parameter = (drug.ProductName,)
        cursor.execute(query, parameter)
        drug_info = cursor.fetchall()
        cursor.close()
        if not drug_info:
            return None
        else:
            drug_info_dictionary = {
                "id": drug_info[0][0],
                "category_id": drug_info[0][1],
                "product_name": drug_info[0][2],
                "price": drug_info[0][3],
                "company_id": drug_info[0][4],
                "description": drug_info[0][5],
                "count": drug_info[0][6],
            }
            return drug_info_dictionary

    def select_drug_by_id(self, drug: DrugModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,category_id, product_name, price, company_id, description, count FROM drugs WHERE id = ?"
        parameter = (drug.DrugId,)
        cursor.execute(query, parameter)
        drug_info = cursor.fetchall()
        cursor.close()
        if not drug_info:
            return None
        else:
            drug_info_dictionary = {
                "id": drug_info[0][0],
                "category_id": drug_info[0][1],
                "product_name": drug_info[0][2],
                "price": drug_info[0][3],
                "company_id": drug_info[0][4],
                "description": drug_info[0][5],
                "count": drug_info[0][6],
            }
            return drug_info_dictionary

    def insert_drug(self, drug: DrugModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO drugs (category_id, product_name, price, company_id, description, count) VALUES (?, ?, ?, ?, ?, ?)"
        parameter = (drug.CategoryId, drug.ProductName, drug.Price, drug.CompanyId, drug.Description, 1)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def update_count_by_id(self, drug_id):
        cursor = self.connection.windows_authentication()
        query = "UPDATE drugs SET count = count+1 WHERE id = ?"
        parameter = (drug_id,)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False