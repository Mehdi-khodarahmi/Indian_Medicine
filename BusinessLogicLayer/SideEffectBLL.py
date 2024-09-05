from DataAccessLayer.SideEffectDAL import CrudSideEffect
from Model.side_effect_model import SideEffectModel
import re


class SideEffectBLL:

    def get_side_effect_id(self, side_effect):
        side_effect_model_obj = SideEffectModel(side_effect_id=0, title=side_effect)
        side_effect_dal_obj = CrudSideEffect()
        side_effect_info = side_effect_dal_obj.select_side_effect_by_title(side_effect=side_effect_model_obj)
        if not side_effect_info:
            side_effect_dal_obj.insert_side_effect(side_effect=side_effect_model_obj)
            side_effect_info = side_effect_dal_obj.select_side_effect_by_title(side_effect=side_effect_model_obj)
        return side_effect_info["id"]

    def get_side_effect_id_list(self, side_effects: str):
        side_effects_list = re.split(r',(?![^(]*\))', side_effects)

        side_effect_list_id = []
        for i in range(len(side_effects_list)):
            side_effect_list_id.append(self.get_side_effect_id(side_effect=side_effects_list[i]))
        return side_effect_list_id
