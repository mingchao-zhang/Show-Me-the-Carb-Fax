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
user_id = "\'" + user_id + "\'"

# Create a cursor that connects to the database, an execute always returns a list
connection = mysql.connect(user=db_user, password=db_password, database=db)
cursor = connection.cursor()

# We enclose it in a try-catch block for efficient error handling
try:
    daily_calories = 0
    daily_carbs = 0
    daily_sugar = 9
    daily_fat = 0
    daily_protein = 0
    daily_sodium = 0
    daily_cholesterol = 0
    
    # Retrieve nutrient information from the recipes table
    query = ("SELECT SUM(R.calories * A.quantity),SUM(R.total_carbs * A.quantity),SUM(R.sugar * A.quantity)"
     ",SUM(R.protein * A.quantity),SUM(R.total_fat * A.quantity),SUM(R.sodium * A.quantity),SUM(R.cholesterol * A.quantity)"
     "FROM recipes AS R, ate as A WHERE R.foodID = A.foodID AND A.username = %s;")
    cursor.execute(query,(user_id,))
    
    for cal,carbs,s,p,f,sod,c in cursor:
    
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
     
"""
    # Retrieve nutrient information from the products table
    query = ("SELECT SUM(P.calories * A.quantity),SUM(P.total_carbs * A.quantity),SUM(P.sugars * A.quantity)"
     ",SUM(P.protein * A.quantity),SUM(P.total_fat * A.quantity),SUM(P.sodium * A.quantity),SUM(P.cholesterol * A.quantity)"
     "FROM products AS P, ate as A WHERE P.foodID = A.foodID AND A.username = %s;")
    cursor.execute(query,(user_id,))
    
    daily_calories += float(cursor[0])
    daily_carbs += float(cursor[1])
    daily_sugar += float(cursor[2])
    daily_protein += float(cursor[3])
    daily_fat += float(cursor[4])
    daily_sodium += float(cursor[5])
    daily_cholesterol += float(cursor[7])
    
    # Retrieve the list of unique dates to compute a per-day average
    query = ("SELECT COUNT(DISTINCT date) FROM ate WHERE username = %s;")
    cursor.execute(query,(user_id,))

    num_days = int(cursor[0])
    
    daily_calories /= num_days
    daily_carbs /= num_days
    daily_sugar /= num_days
    daily_protein /= num_days
    daily_fat /= num_days
    daily_sodium /= num_days
    daily_cholesterol /= num_days

    # Retrieve the targets if applicable
    query = ("SELECT calorie_target,carb_target,fat_target,protein_target FROM users"
    "WHERE username = %s;")
    cursor.execute(query,(user_id,))
    
    
     
    # Retrieve a list of potential recipes i.e. recipes that the user has not consumed
    query = ("SELECT foodID,calories,total_carbs,sugar,protein,total_fat,sodium,cholestrol"
    "FROM recipes WHERE recipes.foodID NOT IN"
    "(SELECT foodID from ate WHERE username = %s);")
    cursor.execute(query,(user_id,))

    recipes = cursor[:]
    
    print(daily_calories)
    print(daily_carbs)
    print(daily_sugar)
    print(daily_protein)
    print(daily_fat)
    print(daily_cholesterol)
    print("Done!")
"""
    connection.close()


except mysql.Error as e:
    print("Error: {}".format(e))


