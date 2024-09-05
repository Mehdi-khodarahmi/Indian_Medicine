from Model.category_model import CategoryModel
from DataAccessLayer.Connection import Connection


class CrudCategory:
    connection = Connection()

    def select_category_by_name(self, category: CategoryModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,name FROM categories WHERE name = ?"
        parameter = (category.CategoryName,)
        cursor.execute(query, parameter)
        category_info = cursor.fetchall()
        cursor.close()
        if not category_info:
            return None
        else:
            category_info_dictionary = {
                "id": category_info[0][0],
                "name": category_info[0][1]
            }
            return category_info_dictionary

    def select_category_by_id(self, category: CategoryModel):
        cursor = self.connection.windows_authentication()
        query = "SELECT id ,name FROM categories WHERE id = ?"
        parameter = (category.CategoryId,)
        cursor.execute(query, parameter)
        category_info = cursor.fetchall()
        cursor.close()
        if not category_info:
            return None
        else:
            category_info_dictionary = {
                "id": category_info[0][0],
                "name": category_info[0][1]
            }
            return category_info_dictionary

    def insert_category(self, category: CategoryModel):
        cursor = self.connection.windows_authentication()
        query = "INSERT INTO categories (name) VALUES (?)"
        parameter = (category.CategoryName,)
        cursor.execute(query, parameter)
        if cursor.commit():
            cursor.close()
            return True
        else:
            cursor.close()
            return False

