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

        
        $searchResults = search_db($string, $dbconnect, $db_name);
        $suggestions_string = '';
        while ($row = mysql_fetch_assoc($searchResults)) {
            $name_and_id = str_replace(' ', '_', $row['name']) . "*" . str_replace(' ', '_', $row['foodId']);
            echo "<div class='food_search_item' id=$name_and_id><p>" . $row['name'] . ", " . $row['foodId'] . "</p></div>";
        }
    }
?>
