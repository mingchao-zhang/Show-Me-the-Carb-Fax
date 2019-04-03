import csv
import json
import os

"""
    All recipes use the following units:
    Users are restricted to the format found in
    https://en.wikipedia.org/wiki/Cooking_weights_and_measures#British_(Imperial)_measures
"""

dataset_file = "epicurious-recipes-with-rating-and-nutrition/full_format_recipes.json"
recipes_file = "recipes.csv" # recip_id,name,description,directions
ingredients_file = "ingredients.csv" # recip_id,ingredient_name,quantity
input_file = "input.txt"
output_file = "results.json"
command = "python bin/parse-ingredients.py input.txt > results.txt && python bin/convert-to-json.py results.txt > results.json"
delimiter = "~"
recipe_id_offset = 5000000

ingredients_output = []
recipe_output = {}

with open(dataset_file) as file:
    data = json.load(file)
    count = 0
    os.chdir("ingredient-phrase-tagger-master/")
    for each_recipe in data:
        if(count > 10):
            break
        try:
            recipe_title = each_recipe["title"].strip()
            key = count + recipe_id_offset
            
            file_content = "\n".join(each_recipe["ingredients"])
            
            with open(input_file, "w") as f:
                f.write(file_content)
            
            os.system(command)
            
            with open(output_file) as f:
                ingredient_data = json.load(f)
            
                for each_ingredient in ingredient_data:
                    name = each_ingredient["name"]
                    unit = ""
                    quantity = ""
                    
                    if('unit' in each_ingredient.keys()):
                        unit = each_ingredient["unit"]
                    if('qty' in each_ingredient.keys()):
                        quantity = each_ingredient["qty"]
                    if('qty' not in each_ingredient.keys()):
                        try:
                            quantity = float(each_ingredient["other"])
                        except:
                            continue

                    line = [str(key),str(name),str(quantity),str(unit)]
                    print(line)
                    ingredients_output.append(line)

            recipe_output[key] = [str(key),str(recipe_title)]
            count += 1
                
        except Exception as e:
            print(e)
            continue

    print(count)
    os.chdir("../")

with open(recipes_file, "w") as output:
    writer = csv.writer(output, delimiter = delimiter,lineterminator='\n')
    for each_recipe in recipe_output.keys():
        line = recipe_output[each_recipe]
        writer.writerow(line)

with open(ingredients_file, "w") as output:
    writer = csv.writer(output, delimiter = delimiter,lineterminator='\n')
    for each_line in ingredients_output:
        writer.writerow(each_line)

