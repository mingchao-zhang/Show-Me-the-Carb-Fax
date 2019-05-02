import csv
import json
import os

"""
    All recipes use the following units:
    Users are restricted to the format found in
    https://en.wikipedia.org/wiki/Cooking_weights_and_measures#British_(Imperial)_measures
"""

dataset_file = "epicurious-recipes-with-rating-and-nutrition/full_format_recipes.json"
recipes_file = "Data/formatted_recipes.csv" # recip_id,name,description,directions
output_file = "Data/descriptions.csv"
delimiter = "~"

descriptions = []
recipes = {}

with open(recipes_file, "r") as f:
    recipe_reader = csv.reader(f, delimiter="~")
    for recipe in recipe_reader:
        recipes[recipe[1]] = recipe
        print(recipe)

with open(dataset_file) as file:
    data = json.load(file)

    for each_recipe in data:
        try:
            recipe_title = each_recipe["title"].strip()

            if(each_recipe["desc"]):
                descriptions.append(recipes[recipe_title] + [each_recipe["desc"]])
            else:
                descriptions.append(recipes[recipe_title] + ["Highly recommended!"])
    
        except Exception as e:
            print(e)


with open(output_file, "w") as output:
    writer = csv.writer(output, delimiter = delimiter,lineterminator='\n')
    for each_recipe in descriptions:
        writer.writerow(each_recipe)
