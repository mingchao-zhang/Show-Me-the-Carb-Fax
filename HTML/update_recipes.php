<?php
    if ( isset($_GET['recipe_name']) && !empty($_GET['recipe_name']) ) {
        // Database Connection
        $dbconnect = mysql_connect("localhost", "root", "carbfax411");
        if(!$dbconnect){
            die('Cannot connect: ' . mysql_error());
        }

        $db_selected = mysql_select_db("411_project_db", $dbconnect);

        if (!$db_selected) {
          die('Cant use database: ' . mysql_error());
        }

        //Get variables
        $recipe_name = $_GET['recipe_name'];
        $recipe_description = $_GET["recipe_description"];
        $item_name = $_GET["item_name"];
        $item_id = $_GET["item_id"];
        $quantity_unit = $_GET["quantity_unit"];
        $quantity = $_GET["quantity"];

        $get_recipe_id_query = "SELECT MAX(foodID) FROM recipes";
        $result = mysql_query($get_recipe_id_query, $dbconnect);
        if (!$result) {
            die("Invalid Query: " . mysql_error());
        }
        $new_recipe_id = mysql_fetch_array($result)[0] + 1;

        $recipe_insert_query = "INSERT INTO recipes (`foodID`, `name`, `calories`, `total_carbs`, `sugar`, `protein`, `total_fat`, `sodium`, `cholesterol`, `directions`) 
        VALUES ('$new_recipe_id', '$recipe_name', 0, 0, 0, 0, 0, 0, 0, '$recipe_description')";
        $result = mysql_query($recipe_insert_query, $dbconnect);
        if (!$result) {
            die("Invalid Query: " . mysql_error());
        }

        # echo the recipe id for insertions into contains table
        echo $new_recipe_id;

        mysql_free_result($result);
        mysql_close($dbconnect);
    }
?>
