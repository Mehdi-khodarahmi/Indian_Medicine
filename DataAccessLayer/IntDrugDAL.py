from Model.int_drug_model import IntDrugModel
from DataAccessLayer.Connection import Connection


class CrudIntDrug:
    connection = Connection()

    def select_int_drug_by_name(self, int_drug: IntDrugModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id, name FROM int_drugs WHERE name = ?"
        parameter = (int_drug.IntDrugName,)
        cursor.execute(query, parameter)
        int_drug_info = cursor.fetchall()
        cursor.close()
        if not int_drug_info:
            return None
        else:
            int_drug_info_dictionary = {
                "id": int_drug_info[0][0],
                "name": int_drug_info[0][1],
            }
            return int_drug_info_dictionary

    def select_int_drug_by_id(self, int_drug: IntDrugModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id, name FROM int_drugs WHERE id = ?"
        parameter = (int_drug.IntDrugId,)
        cursor.execute(query, parameter)
        int_drug_info = cursor.fetchall()
        cursor.close()
        if not int_drug_info:
            return None
        else:
            int_drug_info_dictionary = {
                "id": int_drug_info[0][0],
                "name": int_drug_info[0][1],
            }
            return int_drug_info_dictionary

    def insert_int_drug(self, int_drug: IntDrugModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO int_drugs (name) VALUES (?)"
        parameter = (int_drug.IntDrugName,)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False
