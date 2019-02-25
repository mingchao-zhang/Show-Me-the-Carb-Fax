import csv
import mysql.connector

# The branded food products database
# File names
dcd_file = "BFPD_csv_07132018/Derivation_Code_Description.csv"
nutrients_file = "BFPD_csv_07132018/Nutrients.csv"
products_file = "BFPD_csv_07132018/Products.csv"
servings_file = "BFPD_csv_07132018/Serving_size.csv"

items = {}
results = "BFPD_csv_07132018/results.csv"

with open(products_file, newline='') as f:
    csvreader = csv.reader(f, delimiter = ",")
    num_items = 0
    for row in csvreader:
        num_items += 1
        if(num_items != 1):
            items[int(row[0])] = [int(row[0]),row[1],row[3],1,"Packaging"]

with open(servings_file, newline = '') as f:
    csvreader = csv.reader(f, delimiter = ",")
    num_items = 0
    for row in csvreader:
        num_items += 1
        if(num_items != 1):
            try:
                items[int(row[0])][3] = float(row[1])/100
                items[int(row[0])][4] = row[2]
            except:
                continue

"""
The values are for the quantity found in 100gms or 100 ml
Calories, Carbs, Sugars, Dietary Fiber, Soluble Fiber, InSoluble Fiber, Protein, Total_Fat, Sodium, Cholestrol,
vitaminA,vitaminB6,vitaminB12,vitaminC,vitaminD,vitaminE,niacin,thiamin,calcium,iron,magnesium
phosphorus,potassium,riboflavin,zinc
"""

nutrients = {}
pattern = [208,205,269,291,295,297,203,204,307,601,318,415,418,401,324,340,406,404,301,303,304,305,306,405,309]

with open(nutrients_file,newline = '') as f:
    csvreader = csv.reader(f, delimiter = ",")
    num_items = 0
    
    for i, line in enumerate(csvreader):
        if(i != 0):
            if(int(line[0]) not in nutrients):
                nutrients[int(line[0])] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        try:
            if(int(line[1]) in pattern):
                nutrients[int(line[0])][pattern.index(int(line[1]))] = float(line[4])
        except:
                print(line)


with open(results, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for each_num in nutrients.keys():
            line = items[each_num]
            line += nutrients[each_num]
            writer.writerow(line)

print(len(nutrients))
print(len(items))

mydb = mysql.connector.connect(
                               host="localhost",
                               user="yourusername",
                               passwd="yourpassword",
                               database="mydatabase"
                               )

mycursor = mydb.cursor()
schema = "(foodID,name,upc,serving_size,quantity_units,calories,total_carbs,sugars,dietary_fiber,soluble_fiber,insoluble_fiber,protein,total_fat,sodium,cholesterol,vitaminA,vitaminB6,vitaminB12,vitaminC,vitaminD,vitaminE,niacin,thiamin,calcium,iron,magnesium,phosphorus,potassium,riboflavin,zinc)"
schema_format = "(%u,%s,%s,%f,%s,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)"

with open(results, "r") as data:
    csvreader = csv.reader(data, delimiter = ",")
    for i,line in enumerate(csvreader):
        sql = "INSERT INTO products " + schema + " VALUES " + schema_format
        val = tuple(line)
        mycursor.execute(sql, val)
        mydb.commit()



"""

the_set = set()
with open(results,newline = '') as f:
csvreader = csv.reader(f, delimiter = ",")
for i,line in enumerate(csvreader):
the_set.add(len(line))
if(len(line) == 53 or len(line) == 6):
print(line)

# Init for first element
if(i == 1):
curr = int(line[0])
values= [line[0]]
values.append(line[2] + " " + line[-2] + " " + line[-1])

# When we run out of nutrients for a particular product
elif(int(line[0]) != curr):
num_items += 1
values.append(line[2] + " " + line[-2] + " " + line[-1])
the_line = values[0] + "," + items[int(values[0])] + ","
the_line += ",".join(values[1:])
result_fp.write(the_line + "\n")

curr = int(line[0])
values = [line[0]]
values.append(line[2] + " " + line[-2] + " " + line[-1])

# Otherwise, just add to the current product's list
else:
values.append(line[2] + " " + line[-2] + " " + line[-1])

the_line = values[0] + "," + items[int(values[0])] + ","
the_line += ",".join(values[1:])
result_fp.write(the_line + "\n")
"""
