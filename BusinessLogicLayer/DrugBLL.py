from DataAccessLayer.DrugDAL import CrudDrug
from Model.drug_model import DrugModel


class DrugBLL:

    def get_drug_id(self, drug_info: dict):
        drug_model_obj = DrugModel(drug_id=None, category_id=drug_info["category_id"],
                                   product_name=drug_info["product_name"], price=drug_info["product_price"],
                                   company_id=drug_info["company_id"], description=drug_info["description"],
                                   count=drug_info["count"])
        drug_dal_obj = CrudDrug()
        drug_info = drug_dal_obj.select_drug_by_name(drug=drug_model_obj)
        if drug_info:
            drug_dal_obj.update_count_by_id(drug_info["id"])
        else:
            drug_dal_obj.insert_drug(drug=drug_model_obj)
            drug_info = drug_dal_obj.select_drug_by_name(drug=drug_model_obj)
        return drug_info["id"]
