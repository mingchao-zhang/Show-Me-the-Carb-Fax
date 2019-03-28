import csv
import json


"""
    All recipes use the following units:
    Users are restricted to the format found in
    https://en.wikipedia.org/wiki/Cooking_weights_and_measures#British_(Imperial)_measures
"""

dataset_file = "epicurious-recipes-with-rating-and-nutrition/full_format_recipes.json"
results = "recipes.csv"

ingredients = {}
csv_output = {}

with open(dataset_file) as file:
    data = json.load(file)
    count = 0
    for each_recipe in data:
        try:
            key = each_recipe["title"]
            ingredients[key] = each_recipe["ingredients"]
            csv_output[key] = [key,str(each_recipe["directions"][0])]
            
            count += 1
        
        except:
            continue

    print(count)

with open(results, "w") as output:
    writer = csv.writer(output, delimiter ='~',lineterminator='\n')
    for each_recipe in csv_output.keys():
        line = csv_output[each_recipe]
        writer.writerow(line)

