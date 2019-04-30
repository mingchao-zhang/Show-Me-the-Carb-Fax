<?php
    if ( isset($_GET['name']) && !empty($_GET['name']) ) {
        // Database Connection
        $dbconnect = mysql_connect("localhost", "root", "carbfax411");
        if(!$dbconnect){
            die('Cannot connect: ' . mysql_error());
        }

        $db_selected = mysql_select_db("411_project_db", $dbconnect);

        if (!$db_selected) {
          die('Cant use database: ' . mysql_error());
        }
        echo "Hello?????";
        //echo $_GET['recipe_name'] . " ??? " . $_GET["recipe_description"];   
    }
?>
