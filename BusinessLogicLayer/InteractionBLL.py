import ast
from Model.interactions_model import InteractionsModel
from Model.int_drug_model import IntDrugModel
from Model.int_brand_model import IntBrandModel
from Model.int_effect_model import IntEffectModel
from DataAccessLayer.InteractionDAL import CrudInteraction
from DataAccessLayer.IntDrugDAL import CrudIntDrug
from DataAccessLayer.IntBrandDAL import CrudIntBrand
from DataAccessLayer.IntEffectDAL import CrudIntEffect


class InteractionBLL:

    def separate_dictionary_item(self, interaction: str, drug_id):
        interaction_dict = ast.literal_eval(interaction)
        int_drug_list = interaction_dict["drug"]
        int_brand_list = interaction_dict["brand"]
        int_effect_list = interaction_dict["effect"]
        length_of_drugs = len(int_drug_list)

        for i in range(length_of_drugs):

            # int_drug_id for one index!
            int_drug_name = int_drug_list[i]
            int_drug_model_obj = IntDrugModel(int_drug_id=None, int_drug_name=int_drug_name)
            int_drug_dal_obj = CrudIntDrug()
            int_dug_info = int_drug_dal_obj.select_int_drug_by_name(int_drug_model_obj)
            if not int_dug_info:
                int_drug_dal_obj.insert_int_drug(int_drug_model_obj)
                int_dug_info = int_drug_dal_obj.select_int_drug_by_name(int_drug_model_obj)
            int_drug_id = int_dug_info["id"]

            # int_effect_id for one index!
            int_effect_title = int_effect_list[i]
            int_effect_model_obj = IntEffectModel(int_effect_id=None, int_effect_title=int_effect_title)
            int_effect_dal_obj = CrudIntEffect()
            int_effect_info = int_effect_dal_obj.select_int_effect_by_title(int_effect_model_obj)
            if not int_effect_info:
                int_effect_dal_obj.insert_int_effect(int_effect_model_obj)
                int_effect_info = int_effect_dal_obj.select_int_effect_by_title(int_effect_model_obj)
            int_effect_id = int_effect_info["id"]

            # int_brand_id for one index! --nested
            int_brand_items_list = int_brand_list[i].split(',')
            length_of_brand_item = len(int_brand_items_list)
            for j in range(length_of_brand_item):
                brand_name = int_brand_items_list[j].strip()
                int_brand_model_obj = IntBrandModel(int_brand_id=None, int_brand_name=brand_name,
                                                    int_drug_id=int_drug_id)
                int_brand_dal_obj = CrudIntBrand()
                brand_info = int_brand_dal_obj.select_int_brand_by_name_and_int_drug_id(int_brand_model_obj)
                if not brand_info:
                    int_brand_dal_obj.insert_brand(int_brand_model_obj)
                    brand_info = int_brand_dal_obj.select_int_brand_by_name_and_int_drug_id(int_brand_model_obj)
                brand_id = brand_info["id"]

                # interation
                interaction_model_obj = InteractionsModel(int_brand_id=brand_id, drug_id=drug_id,
                                                          int_effect_id=int_effect_id)
                interaction_dal_obj = CrudInteraction()
                interaction_info = interaction_dal_obj.select_interaction(interaction_model_obj)
                if not interaction_info:
                    interaction_dal_obj.insert_interactions(interaction_model_obj)
                    interaction_info = interaction_dal_obj.select_interaction(interaction_model_obj)
        return True
