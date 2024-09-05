from Model.side_effect_model import SideEffectModel
from DataAccessLayer.Connection import Connection


class CrudSideEffect:
    connection = Connection()

    def select_side_effect_by_title(self, side_effect: SideEffectModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,title FROM side_effects WHERE title = ?"
        parameter = (side_effect.Title,)
        cursor.execute(query, parameter)
        side_effect_info = cursor.fetchall()
        cursor.close()
        if not side_effect_info:
            return None
        else:
            side_effect_info_dictionary = {
                "id": side_effect_info[0][0],
                "title": side_effect_info[0][1]
            }
            return side_effect_info_dictionary

    def select_side_effect_by_id(self, side_effect: SideEffectModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,title FROM side_effects WHERE id = ?"
        parameter = (side_effect.SideEffectId,)
        cursor.execute(query, parameter)
        side_effect_info = cursor.fetchall()
        cursor.close()
        if not side_effect_info:
            return None
        else:
            side_effect_info_dictionary = {
                "id": side_effect_info[0][0],
                "title": side_effect_info[0][1]
            }
            return side_effect_info_dictionary

    def insert_side_effect(self, side_effect: SideEffectModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO side_effects (title) VALUES (?)"
        parameter = (side_effect.Title,)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False

