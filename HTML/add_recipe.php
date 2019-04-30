<?php
    echo "line 2";
    if ( isset($_GET['recipe_name']) && !empty($_GET['recipe_name']) ) {
        // Database Connection
        echo "line 5";
        $dbconnect = mysql_connect("localhost", "root", "carbfax411");
        if(!$dbconnect){
            die('Cannot connect: ' . mysql_error());
        }

        echo "line 11";
        $db_selected = mysql_select_db("411_project_db", $dbconnect);

        if (!$db_selected) {
          die('Cant use database: ' . mysql_error());
        }
        echo "Hello?????";
        //echo $_GET['recipe_name'] . " ??? " . $_GET["recipe_description"];   
    }
?>
