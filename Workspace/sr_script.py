import csv
import re
#import mysql.connector

# Files for the standard reference database


desc_file = "SR-Leg_ASC/FOOD_DES.txt"
nutrients_file = "SR-Leg_ASC/NUT_DATA.txt"
fdgrps_file = "SR-Leg_ASC/FD_GROUP.txt"
weights_file = "SR-Leg_ASC/WEIGHT.txt"
results = "sr.csv"

items = {}
groups = {}

def remove_char(line):
    return re.sub('~', '', line)

def process(string):
    return re.sub('"','',string)

def process_row(list):
    for i in range(len(list)):
        list[i] = remove_char(list[i])
    return list

with open(fdgrps_file, newline='') as f:
    csvreader = csv.reader(f, delimiter = "^")
    for row in csvreader:
        groups[int(remove_char(row[0]))] = process(row[1])

with open(desc_file, newline = '',encoding = "ISO-8859-1") as f:
    csvreader = csv.reader(f, delimiter = "^")
    num_items = 0
    
    for row in csvreader:
        try:
            num_items += 1
            items[int(remove_char(row[0]))] = [int(remove_char(row[0])),remove_char(row[2]),groups[int(remove_char(row[1]))]]
        except:
            print("Error!")

"""
    The values are for the quantities found in 100gms or 100 ml
    calories, carbs, sugars, dietary fiber, soluble fiber, inSoluble fiber, protein, total_fat, sodium, cholestrol,
    vitaminA,vitaminB6,vitaminB12,vitaminC,vitaminD,vitaminE,niacin,thiamin,calcium,iron,magnesium
    phosphorus,potassium,riboflavin,zinc
"""

nutrients = {}
pattern = [208,205,269,291,295,297,203,204,307,601,318,415,418,401,324,340,406,404,301,303,304,305,306,405,309]

with open(nutrients_file,newline = '') as f:
    csvreader = csv.reader(f, delimiter = "^")
    num_items = 0

    for i, line in enumerate(csvreader):
        line = process_row(line)
        if(int(line[0]) not in nutrients):
            nutrients[int(line[0])] = [0]*25
        try:
            if(int(line[1]) in pattern):
                nutrients[int(line[0])][pattern.index(int(line[1]))] = float(line[2])
        
        except Exception as e:
            print(line)
            print(str(e))
            pass


with open(results, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for each_num in nutrients.keys():
        line = items[each_num]
        line += nutrients[each_num]
        writer.writerow(line)

print("Num records: " + str(len(nutrients)))

mydb = mysql.connector.connect(
                               host="localhost",
                               user="yourusername",
                               passwd="yourpassword",
                               database="mydatabase"
                               )

mycursor = mydb.cursor()
schema = "(foodID,name,food_group,calories,total_carbs,sugars,dietary_fiber,soluble_fiber,insoluble_fiber,protein,total_fat,sodium,cholesterol,vitaminA,vitaminB6,vitaminB12,vitaminC,vitaminD,vitaminE,niacin,thiamin,calcium,iron,magnesium,phosphorus,potassium,riboflavin,zinc)"
schema_format = "(%u,%s,%s,%f,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"

with open(results, "r") as data:
    csvreader = csv.reader(data, delimiter = ",")
    for i,line in enumerate(csvreader):
        sql = "INSERT INTO products " + schema + " VALUES " + schema_format
        val = tuple(line)
        mycursor.execute(sql, val)
        mydb.commit()

