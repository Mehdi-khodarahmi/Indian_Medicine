from DataAccessLayer.SaltDAL import CrudSalt
from Model.salt_model import SaltModel


class SaltBLL:

    def get_salt_id(self, salt_name):
        salt_model_obj = SaltModel(salt_id=0, salt_name=salt_name)
        salt_dal_obj = CrudSalt()
        salt_info = salt_dal_obj.select_salt_by_name(salt=salt_model_obj)
        if not salt_info:
            salt_dal_obj.insert_salt(salt=salt_model_obj)
            salt_info = salt_dal_obj.select_salt_by_name(salt=salt_model_obj)
        return salt_info["id"]

    def get_salt_id_list(self, salts: str):
        salt_list = salts.split("+")
        salt_list_id = []
        for i in range(len(salt_list)):
            salt_list_id.append(self.get_salt_id(salt_name=salt_list[i].strip()))
        return salt_list_id


