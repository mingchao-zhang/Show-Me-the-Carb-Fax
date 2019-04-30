"""
    <?php
    $command = escapeshellcmd('python recommendations.py user-ids');
    $output = shell_exec($command);
    echo $output;
    ?>
    
    Code like snippet the above can be used to extract the recommended recipes. Simply printing
    the id's of recommended recipes is sufficient. The input-id is given as the first command
    line argument
    
    Our recommendations are based on the following nutrients:
    calories,total_carbs,sugar,protein,total_fat,sodium,cholesterol
    
"""

import sys
import mysql.connector as mysql

db_user = "root"
db_password = "carbfax411"
db = "411_project_db"
user_id = sys.argv[1] # The id of the user as a string

# Create a cursor that connects to the database, an execute always returns a list
connection = mysql.connect(user=db_user, password=db_password, database=db)
cursor = connection.cursor()

# We enclose it in a try-catch block for efficient error handling
try:
    daily_calories = 0
    daily_carbs = 0
    daily_sugar = 0
    daily_fat = 0
    daily_protein = 0
    daily_sodium = 0
    daily_cholesterol = 0
    
    # Retrieve nutrient information from the recipes table
    query = ("SELECT SUM(R.calories * A.quantity),SUM(R.total_carbs * A.quantity),SUM(R.sugar * A.quantity)"
     ",SUM(R.protein * A.quantity),SUM(R.total_fat * A.quantity),SUM(R.sodium * A.quantity),SUM(R.cholesterol * A.quantity)"
     "FROM recipes AS R, ate as A WHERE R.foodID = A.foodID AND A.username = %s;")
    cursor.execute(query,(user_id,))
    
    for (cal,carbs,s,p,f,sod,c) in cursor:
        
        if(cal):
            daily_calories += float(cal)
        if(carbs):
            daily_carbs += float(carbs)
        if(s):
            daily_sugar += float(s)
        if(p):
            daily_protein += float(p)
        if(f):
            daily_fat += float(f)
        if(sod):
            daily_sodium += float(sod)
        if(c):
           daily_cholesterol += float(c)
     

    # Retrieve nutrient information from the products table
    query = ("SELECT SUM(P.calories * A.quantity),SUM(P.total_carbs * A.quantity),SUM(P.sugars * A.quantity)"
     ",SUM(P.protein * A.quantity),SUM(P.total_fat * A.quantity),SUM(P.sodium * A.quantity),SUM(P.cholesterol * A.quantity)"
     "FROM products AS P, ate as A WHERE P.foodID = A.foodID AND A.username = %s;")
    cursor.execute(query,(user_id,))

    for (cal,carbs,s,p,f,sod,c) in cursor:

        if(cal):
            daily_calories += float(cal)
        if(carbs):
            daily_carbs += float(carbs)
        if(s):
            daily_sugar += float(s)
        if(p):
            daily_protein += float(p)
        if(f):
            daily_fat += float(f)
        if(sod):
            daily_sodium += float(sod)
        if(c):
            daily_cholesterol += float(c)

    # Retrieve the list of unique dates to compute a per-day average
    query = ("SELECT COUNT(DISTINCT (EXTRACT(DAY FROM date))) FROM ate WHERE username = %s;")
    cursor.execute(query,(user_id,))
    
    for (days,) in cursor:
        num_days = int(days)

    daily_calories /= num_days
    daily_carbs /= num_days
    daily_sugar /= num_days
    daily_protein /= num_days
    daily_fat /= num_days
    daily_sodium /= num_days
    daily_cholesterol /= num_days

#    # Retrieve the targets if applicable
    query = ("SELECT calorie_target,carb_target,fat_target,protein_target FROM users "
    "WHERE username = %s;")
    cursor.execute(query,(user_id,))

    cal_target = 0
    carb_target = 0
    fat_target = 0
    prot_target = 0

    for  (c1,c2,f,p) in cursor:

        if(c1):
            cal_target = cal
        if(c2):
            carb_target = carbs
        if(f):
            fat_target = f
        if(p):
            prot_target = p

    query = "SELECT age,height,weight WHERE username = %s;"
    cursor.execute(query,(user_id,))

    a = 0
    h = 0
    w = 0
    for (a,h,w) in cursor:
        age = float(a)
        height = float(h)*2.54
        weight = float(w)*0.453592;


    cals_recmnd = ceil((10 * weight) + (6.25 *height) - (5 * age) + 5);
    carbs_recmnd = ceil(cals_recmnd * 0.5 / 4);
    prot_recmnd = ceil(cals_recmnd * 0.25 / 4);
    fat_recmnd = ceil(cals_recmnd * 0.25 / 9);

    # Retrieve a list of potential recipes i.e. recipes that the user has not consumed
    query = ("SELECT foodID,calories,total_carbs,sugar,protein,total_fat,sodium,cholesterol "
    "FROM recipes WHERE recipes.foodID NOT IN "
    "(SELECT foodID from ate WHERE username = %s);")
    cursor.execute(query,(user_id,))
    recipes = []

    for recipe in cursor:
        recipes.append(recipe)

    # We recommend those recipes that minimize the mean-square distance between the various nutrient values
    # We assume that the standard portion is about 500 calories
    
    
    
    print(daily_calories)
    print(daily_carbs)
    print(daily_sugar)
    print(daily_protein)
    print(daily_fat)
    print(daily_cholesterol)
    print("Done!")

    connection.close()


except mysql.Error as e:
    print("Error: {}".format(e))


