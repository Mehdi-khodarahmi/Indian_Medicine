from Model.int_brand_model import IntBrandModel
from DataAccessLayer.Connection import Connection


class CrudIntBrand:
    connection = Connection()

    def select_int_brand_by_name_and_int_drug_id(self, int_brand: IntBrandModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,brand_name, int_drug_id FROM int_brands WHERE brand_name = ? AND int_drug_id = ?"
        parameter = (int_brand.IntBrandName, int_brand.IntDrugId)
        cursor.execute(query, parameter)
        int_brand_info = cursor.fetchall()
        cursor.close()
        if not int_brand_info:
            return None
        else:
            int_brand_info_dictionary = {
                "id": int_brand_info[0][0],
                "brand_name": int_brand_info[0][1],
                "int_drug_id": int_brand_info[0][2]
            }
            return int_brand_info_dictionary

    def select_int_brand_by_id(self, int_brand: IntBrandModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,brand_name, int_drug_id FROM int_brands WHERE id = ?"
        parameter = (int_brand.IntBrandId,)
        cursor.execute(query, parameter)
        int_brand_info = cursor.fetchall()
        cursor.close()
        if not int_brand_info:
            return None
        else:
            int_brand_info_dictionary = {
                "id": int_brand_info[0][0],
                "brand_name": int_brand_info[0][1],
                "int_drug_id": int_brand_info[0][2]
            }
            return int_brand_info_dictionary

    def insert_brand(self, int_brand: IntBrandModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO int_brands (brand_name, int_drug_id) VALUES (?, ?)"
        parameter = (int_brand.IntBrandName, int_brand.IntDrugId)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False
