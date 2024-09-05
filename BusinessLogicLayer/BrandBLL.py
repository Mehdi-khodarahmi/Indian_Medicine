from ast import literal_eval
from DataAccessLayer.IntBrandDAL import CrudIntBrand
from Model.int_brand_model import IntBrandModel


class BrandtBLL:
    pass
    # def get_brand_list_effect_with_id(self, brands: str):
    #     brand_dict = literal_eval(brands)
    #     items_len = len(brand_dict["drug"])
    #     if items_len == 0:
    #         return None
    #     else:
    #         effect_dict = {}
    #         for i in range(items_len):
    #             drug_name = brand_dict["drug"][i]
    #             brand_name = brand_dict["brand"][i]
    #             brand_id = self.get_brand_id(drug_name=drug_name, brand_name=brand_name)
    #             effect_name = brand_dict["effect"][i]
    #             effect_dict[brand_id] = effect_name
    #         return effect_dict
    #
    # def get_brand_id(self, brand_name, drug_id):
    #     brand_model_obj = IntBrandModel(int_brand_id=None, int_drug_id=drug_id, int_brand_name=brand_name)
    #     brand_dal_obj = CrudBrand()
    #     brand_info = brand_dal_obj.select_brand_by_name(brand=brand_model_obj)
    #     if not brand_info:
    #         brand_dal_obj.insert_brand(brand=brand_model_obj)
    #         brand_info = brand_dal_obj.select_brand_by_name(brand=brand_model_obj)
    #     return brand_info["id"]