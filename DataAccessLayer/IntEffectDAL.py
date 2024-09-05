from Model.int_effect_model import IntEffectModel
from DataAccessLayer.Connection import Connection


class CrudIntEffect:
    connection = Connection()

    def select_int_effect_by_title(self, int_effect: IntEffectModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id, title FROM int_effects WHERE title = ?"
        parameter = (int_effect.IntEffectTitle,)
        cursor.execute(query, parameter)
        int_effect_info = cursor.fetchall()
        cursor.close()
        if not int_effect_info:
            return None
        else:

            int_effect_info_dictionary = {
                "id": int_effect_info[0][0],
                "title": int_effect_info[0][1],
            }
            return int_effect_info_dictionary

    def select_int_effect_by_id(self, int_effect: IntEffectModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id, title FROM int_effects WHERE id = ?"
        parameter = (int_effect.IntEffectId,)
        cursor.execute(query, parameter)
        int_effect_info = cursor.fetchall()
        cursor.close()
        if not int_effect_info:
            return None
        else:

            int_effect_info_dictionary = {
                "id": int_effect_info[0][0],
                "title": int_effect_info[0][1],
            }
            return int_effect_info_dictionary

    def insert_int_effect(self, int_effect: IntEffectModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO int_effects (title) VALUES (?)"
        parameter = (int_effect.IntEffectTitle,)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False
