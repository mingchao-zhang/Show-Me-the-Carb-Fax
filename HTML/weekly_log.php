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
        $id = $row['ID'];
        echo "<tr>";
        echo "<td>" . $row['name'] . "</td>";
        echo "<td>" . $row['ID'] . "</td>";
        echo "<td>" . $row['date'] . "</td>";
        echo "<td>" . 
        "<button name='remove' class='btn btn-sm btn-primary btn-block weekly_log_plus_button' type='submit' id=$id>+</button>"
        . $row['quantity'] 
        . "<button name='remove' class='btn btn-sm btn-primary btn-block weekly_log_minus_button' type='submit' id=$id>-</button>"
        . "</td>";
        echo "</tr>";
    }


    // Close Database Connection
    mysql_free_result($ateResult);
    mysql_close($dbconnect);
?>