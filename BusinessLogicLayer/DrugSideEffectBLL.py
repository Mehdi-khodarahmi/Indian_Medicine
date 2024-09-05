from Model.drug_side_effect_model import DrugSideEffectModel
from DataAccessLayer.DrugSideEffectDAL import CrudDrugSideEffect

class DrugSideEffectBLL:

    def insert_drug_side_effect(self, drug_id, side_effect_id):
        drug_side_effect_model_obj = DrugSideEffectModel(drug_id=drug_id, side_effect_id=side_effect_id)
        drug_side_effect_dal_obj = CrudDrugSideEffect()
        drug_side_effect_info = drug_side_effect_dal_obj.select_drug_side_effect(
            drug_side_effect=drug_side_effect_model_obj)
        if not drug_side_effect_info:
            drug_side_effect_dal_obj.insert_drug_side_effect(drug_side_effect=drug_side_effect_model_obj)
            drug_side_effect_info = drug_side_effect_dal_obj.select_drug_side_effect(
                drug_side_effect=drug_side_effect_model_obj)
        return drug_side_effect_info


