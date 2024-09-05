from Model.interactions_model import InteractionsModel
from DataAccessLayer.Connection import Connection


class CrudInteraction:
    connection = Connection()

    def select_interaction(self, interaction: InteractionsModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT int_brand_id, drug_id ,int_effect_id FROM interactions WHERE int_brand_id = ? AND drug_id = ? and int_effect_id = ?"
        parameter = (interaction.IntBrandId, interaction.DrugId, interaction.IntEffectId)
        cursor.execute(query, parameter)
        interaction_info = cursor.fetchall()
        cursor.close()
        if not interaction_info:
            return None
        else:
            interaction_info_dictionary = {
                "int_brand_id": interaction_info[0][0],
                "drug_id": interaction_info[0][1],
                "int_effect_id": interaction_info[0][2],
            }
            return interaction_info_dictionary

    def insert_interactions(self, interaction: InteractionsModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO interactions (drug_id, int_brand_id, int_effect_id) VALUES (?, ?, ?)"
        parameter = (interaction.DrugId, interaction.IntBrandId, interaction.IntEffectId)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False
