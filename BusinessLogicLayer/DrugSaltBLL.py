from DataAccessLayer.DrugSaltDAL import CrudDrugSalt
from Model.drug_salt_model import DrugSaltModel


class DrugSaltBLL:

    def insert_drug_salt_id(self, drug_id, salt_id):
        drug_salt_model_obj = DrugSaltModel(drug_id=drug_id, salt_id=salt_id, quantity=None, unit=None)
        drug_salt_dal_obj = CrudDrugSalt()
        drug_salt_info = drug_salt_dal_obj.select_drug_salt(drug_salt=drug_salt_model_obj)
        if not drug_salt_info:
            drug_salt_dal_obj.insert_drug_salt(drug_salt=drug_salt_model_obj)
            drug_salt_info = drug_salt_dal_obj.select_drug_salt(drug_salt=drug_salt_model_obj)
        return drug_salt_info
