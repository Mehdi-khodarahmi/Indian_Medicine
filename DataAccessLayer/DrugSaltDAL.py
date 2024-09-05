from Model.drug_salt_model import DrugSaltModel
from DataAccessLayer.Connection import Connection


class CrudDrugSalt:
    connection = Connection()

    def select_drug_salt(self, drug_salt: DrugSaltModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT drug_id, salt_id, quantity ,unit FROM drug_salts WHERE drug_id = ? AND salt_id = ?"
        parameter = (drug_salt.DrugId, drug_salt.SaltId)
        cursor.execute(query, parameter)
        drug_salt_info = cursor.fetchall()
        cursor.close()
        if not drug_salt_info:
            return None
        else:
            drug_salt_info_dictionary = {
                "drug_id": drug_salt_info[0][0],
                "salt_id": drug_salt_info[0][1],
                "quantity": drug_salt_info[0][2],
                "unit": drug_salt_info[0][3]
            }
            return drug_salt_info_dictionary

    def insert_drug_salt(self, drug_salt: DrugSaltModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO drug_salts (drug_id, salt_id, quantity ,unit) VALUES (?, ?, ?, ?)"
        parameter = (drug_salt.DrugId, drug_salt.SaltId, drug_salt.Quantity, drug_salt.Unit)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False
