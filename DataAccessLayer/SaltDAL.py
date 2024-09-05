from Model.salt_model import SaltModel
from DataAccessLayer.Connection import Connection


class CrudSalt:
    connection = Connection()

    def select_salt_by_name(self, salt: SaltModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,name FROM salts WHERE name = ?"
        parameter = (salt.SaltName,)
        cursor.execute(query, parameter)
        salt_info = cursor.fetchall()
        cursor.close()
        if not salt_info:
            return None
        else:
            salt_info_dictionary = {
                "id": salt_info[0][0],
                "name": salt_info[0][1]
            }
            return salt_info_dictionary

    def select_salt_by_id(self, salt: SaltModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,name FROM salts WHERE id = ?"
        parameter = (salt.SaltId,)
        cursor.execute(query, parameter)
        salt_info = cursor.fetchall()
        cursor.close()
        if not salt_info:
            return None
        else:
            salt_info_dictionary = {
                "id": salt_info[0][0],
                "name": salt_info[0][1]
            }
            return salt_info_dictionary

    def insert_salt(self, salt: SaltModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO salts (name) VALUES (?)"
        parameter = (salt.SaltName,)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False

