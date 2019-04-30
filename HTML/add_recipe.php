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
        echo $_GET['recipe_name'] . " " . $_GET["recipe_description"] . " " . $_GET["item_name"] . " " . $_GET["item_id"] . " " . $_GET["quantity_unit"] . " " . $_GET["quantity"];
    }
?>
