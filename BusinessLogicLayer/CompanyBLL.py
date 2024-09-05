from DataAccessLayer.CompanyDAL import CrudCompany
from Model.company_model import CompanyModel


class CompanyBLL:

    def get_company_id(self, company_name):
        company_model_obj = CompanyModel(company_id=None, company_name=company_name)
        company_dal_obj = CrudCompany()
        company_info = company_dal_obj.select_company_by_name(company=company_model_obj)
        if not company_info:
            company_dal_obj.insert_company(company=company_model_obj)
            company_info = company_dal_obj.select_company_by_name(company=company_model_obj)
        return company_info["id"]

