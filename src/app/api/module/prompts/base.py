from textwrap import dedent

base_prompt = dedent("""
        ### Instruction:
        
        product description starts here

        {text}

        product description ends here

        this is the categorys list ['BEVERAGES', 'SNACKS & BRANDED FOODS', 'NOT FOUND', 'EGGS, MEAT & FISH', 'FOODGRAINS, OIL & MASALA', 'PERSONAL CARE', 'CLEANING & HOUSEHOLD', 'FRUITS & VEGETABLES', 'BAKERY, CAKES & DAIRY', 'MAKEUP', 'BABY CARE', 'PET FOOD & ACCESSORIES', 'NON FMCG', 'ALCOHOL & TOBACCO', 'WELLNESS', 'EVERYDAY MEDICINE-NEW', 'EXCERCISE & FITNESS', 'ALCOHOLIC BEVERAGES'].

        Get the text from the product image and the above product description to give me the following details in JSON format:
        ( return "null" where you don't have a answer)
        
        "brand": "sample_brand",
        "mrp": "The price might start with MRP or Rs.",
        "price": "The price might start with MRP or Rs.",
        "unit": "per pack",
        "Quantity": 1,  ## num of products visible in the image
        "parent_category": "from the above given list",
        "marketed_by": "sample_marketer",
        "manufactured_by": "sample_manufacturer",
        "manufactured_in_country": "Country XYZ",
        "type_of_packaging": "Box",
        "promotion_on_the_pack": "if any",
        "type_of_product": "give this your understanding",
        "pack_of_or_no_of_units": "No. of Units"
        "description" : "Generate a description of the product"
        "weight" : "If the weight is mentioned in the Image or OCR Text"
        
        Analyse data from the above product description to give me the following details in JSON format:
        Only return the output in the required json format.
        """)


gpt3 = dedent(""" I am providing you with a OCR text about a product.

              OCR TEXT : {text}
              I want you to provide me with the name of prodcut in following JSON format:
               "product_name" : "BRU instant coffee".
              
              """)


voice_edit = dedent("""
        ### Instruction: 
        audio transcription starts here
        {text}
        audio transcription ends here
        
        I want you to provide the json format with all the details filled as mentioned below by getting information from the audio transcription.
        ( return "null" where you don't have a answer)
        
        "brand": "sample_brand",
        "mrp": "12", ##price of product
        "unit": "per pack",
        "Quantity": 1,  ##num of products visible
        "parent_category": "from the above given list",
        "ingredients": ["ingredient1", "ingredient2", "ingredient3"],
        "calorie_count": "Would be in numbers",
        "marketed_by": "sample_marketer",
        "manufactured_by": "sample_manufacturer",
        "manufactured_in_country": "Country XYZ",
        "type_of_packaging": "Box",
        "promotion_on_the_pack": "if any",
        "type_of_product": "give this your understanding",
        "pack_of_or_no_of_units": "No. of Units"
     
        Only return the output in the required json format with string in enclosed in double quotes.
        """)