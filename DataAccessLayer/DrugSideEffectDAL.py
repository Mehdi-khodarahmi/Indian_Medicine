from Model.drug_side_effect_model import DrugSideEffectModel
from DataAccessLayer.Connection import Connection


class CrudDrugSideEffect:
    connection = Connection()

    def select_drug_side_effect(self, drug_side_effect: DrugSideEffectModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT drug_id, side_effect_id FROM drug_side_effects WHERE drug_id = ? AND side_effect_id = ?"
        parameter = (drug_side_effect.DrugId, drug_side_effect.SideEffectId)
        cursor.execute(query, parameter)
        drug_side_effect_info = cursor.fetchall()
        cursor.close()
        if not drug_side_effect_info:
            return None
        else:
            drug_side_effect_info_dictionary = {
                "drug_id": drug_side_effect_info[0][0],
                "side_effect_id": drug_side_effect_info[0][1],
            }
            return drug_side_effect_info_dictionary

    def insert_drug_side_effect(self, drug_side_effect: DrugSideEffectModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO drug_side_effects (drug_id, side_effect_id) VALUES (?, ?)"
        parameter = (drug_side_effect.DrugId, drug_side_effect.SideEffectId)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False

