from DataAccessLayer.CategoryDAL import CrudCategory
from Model.category_model import CategoryModel


class CategoryBLL:

    def get_category_id(self, category_name):
        category_model_obj = CategoryModel(category_id=0, category_name=category_name)
        category_dal_obj = CrudCategory()
        category_info = category_dal_obj.select_category_by_name(category=category_model_obj)
        if not category_info:
            category_dal_obj.insert_category(category=category_model_obj)
            category_info = category_dal_obj.select_category_by_name(category=category_model_obj)
        return category_info["id"]

