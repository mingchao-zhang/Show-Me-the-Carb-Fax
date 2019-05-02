<?php
    // Database Connection
    $dbconnect = mysql_connect("localhost", "root", "carbfax411");
    if ( !$dbconnect ) {
        die('Cannot connect: ' . mysql_error());
    }

    $db_selected = mysql_select_db("411_project_db", $dbconnect);
    if ( !$db_selected ) {
        die('Cant use database: ' . mysql_error());
    }

    // Query to Get Eaten Items
    $queryAte = "SELECT products.name AS name, ate.foodID AS ID, ate.date AS date, ate.quantity AS quantity FROM ate, products WHERE username = '$username' and ate.foodID = products.foodID";
    $ateResult = mysql_query($queryAte, $dbconnect);

    if ( !$ateResult ) {
        die('Invalid Query: ' . mysql_error());
    }

    while ( $row = mysql_fetch_assoc($ateResult) ) {
        $food_id = $row['ID'];
        $date = $row['date'];
        $row_id = $username . "&" . $food_id . "&" . $date;
        echo "<tr>";
        echo "<td>" . $row['name'] . "</td>";
        echo "<td>" . $row['ID'] . "</td>";
        echo "<td>" . $row['date'] . "</td>";
        echo "<td>" . 
        "<button name='remove' class='btn btn-sm btn-primary btn-block weekly_log_plus_button' type='submit' id=$row_id>+</button>"
        . $row['quantity'] 
        . "<button name='remove' class='btn btn-sm btn-primary btn-block weekly_log_minus_button' type='submit' id=$row_id>-</button>"
        . "</td>";
        echo "</tr>";
    }
    $queryRecipes = "SELECT recipes.name, ate.foodID, ate.date, ate.quantity FROM ate, recipes WHERE username = '$username' and ate.foodID = recipes.foodID";
    $recipeResult = mysql_query($queryRecipes, $dbconnect);

    if (!$recipeResult){
        die("Invalid Query:" . mysql_error());
    }
    while ( $row = mysql_fetch_assoc($recipeResult) ) {
        $food_id = $row['ate.foodID'];
        $date = $row['ate.date'];
        $row_id = $username . "&" . $food_id . "&" . $date;
        echo "<tr>";
        echo "<td>" . $row['recipes.name'] . "</td>";
        echo "<td>" . $row['ate.foodID'] . "</td>";
        echo "<td>" . $row['ate.date'] . "</td>";
        echo "<td>" . 
        "<button name='remove' class='btn btn-sm btn-primary btn-block weekly_log_plus_button' type='submit' id=$row_id>+</button>"
        . $row['ate.quantity'] 
        . "<button name='remove' class='btn btn-sm btn-primary btn-block weekly_log_minus_button' type='submit' id=$row_id>-</button>"
        . "</td>";
        echo "</tr>";
    }
    // Close Database Connection
    mysql_free_result($ateResult);
    mysql_free_result($recipeResult);
    mysql_close($dbconnect);
?>