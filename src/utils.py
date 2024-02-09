import json

with open('Category-tree.json') as f:
    cat_data = json.load(f)
    
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