import pandas as pd
from BusinessLogicLayer.CategoryBLL import CategoryBLL
from BusinessLogicLayer.SaltBLL import SaltBLL
from BusinessLogicLayer.DrugBLL import DrugBLL
from BusinessLogicLayer.DrugSaltBLL import DrugSaltBLL
from BusinessLogicLayer.DrugSideEffectBLL import DrugSideEffectBLL
from BusinessLogicLayer.InteractionBLL import InteractionBLL
from BusinessLogicLayer.CompanyBLL import CompanyBLL
from BusinessLogicLayer.SideEffectBLL import SideEffectBLL


df = pd.read_csv('Files/DataSource/medicine_data.csv')
for i in range(len(df)):
    drug_dict = {}

    # category
    category = df["sub_category"].iloc[i]
    category_bll_object = CategoryBLL()
    drug_dict["category_id"] = category_bll_object.get_category_id(category_name=category)

    # product_name
    product_name = df["product_name"].iloc[i]
    drug_dict["product_name"] = product_name

    # product_price
    price = df["product_price"].iloc[i]
    if isinstance(price, float):
        drug_dict["product_price"] = 0
    else:
        price = price.replace("â‚¹", "").replace("₹", "")
        drug_dict["product_price"] = float(price)

    # product_manufactured
    company = df["product_manufactured"].iloc[i]
    company_bll_object = CompanyBLL()
    drug_dict["company_id"] = company_bll_object.get_company_id(company_name=company)

    # medicine_desc
    description = df["medicine_desc"].iloc[i]
    drug_dict["description"] = description

    # count
    drug_dict["count"] = None

    # >> get_dug_id
    drug_id = DrugBLL().get_drug_id(drug_info=drug_dict)

    # salt
    salts = df["salt_composition"].iloc[i]
    salts_id_list = SaltBLL().get_salt_id_list(salts=salts)
    for j in range(len(salts_id_list)):
        salt_id = salts_id_list[j]
        DrugSaltBLL().insert_drug_salt_id(drug_id, salts_id_list[j])

    # side_effects
    side_effects = df["side_effects"].iloc[i]
    side_effect_object = SideEffectBLL()
    side_effects_list = side_effect_object.get_side_effect_id_list(side_effects=side_effects)
    for k in range(len(side_effects_list)):
        DrugSideEffectBLL().insert_drug_side_effect(drug_id=drug_id, side_effect_id=side_effects_list[k])

    # drug_interactions
    interactions = df["drug_interactions"].iloc[i]
    interaction = InteractionBLL().separate_dictionary_item(interactions, drug_id)

    sep = "-"*100
    print(f"Item No.{i+1} Successfully processed (Inserted/Updated).\nInfo: {drug_dict}\n{sep}")
