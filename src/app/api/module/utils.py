import json

# with open('Category-tree.json') as f:
#     cat_data = json.load(f)
    
candidate_labels = ['BEVERAGES', 'SNACKS & BRANDED FOODS', 'NOT FOUND', 'EGGS, MEAT & FISH', 
		    'FOODGRAINS, OIL & MASALA', 'PERSONAL CARE', 'CLEANING & HOUSEHOLD', 
		    'FRUITS & VEGETABLES', 'BAKERY, CAKES & DAIRY', 'MAKEUP', 'BABY CARE', 
		    'PET FOOD & ACCESSORIES', 'NON FMCG', 'TOBACCO', 'WELLNESS', 'ALCOHOLIC BEVERAGES']

def get_childs(parent):
    catagories = []
    for category in cat_data:
        if category['name'] == parent:
            for child in category['children']:
                catagories.append(child['name'])
    return catagories

def get_inner_child(to_find_parent,to_find_child):
    catagories = []
    for parent in cat_data:
        if parent['name'] == to_find_parent:
            for child in parent['children']:
                if child['name'] == to_find_child:
                    for inner_child in child['children']:
                        catagories.append(inner_child['name'])
    return catagories



def extract_json_from_text(text):
    text = str(text)
    
    try:
        # Find the JSON part within the text
        start_index = text.find('{')
        end_index = text.rfind('}') + 1
        json_part = text[start_index:end_index]
        json_part = json.loads(json_part.strip())
        return json_part

    except Exception as e:
        print(f"\033[31m Exception occurred while loading JSON: {str(e)} [0m")
        return e