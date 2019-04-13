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

    //get parameters
    $username = $_GET['username'];
    $id = $_GET['id'];
    $date = $_GET['date'];
    $add = intval($_GET['add']);
    echo $username . $id . $date . $add;
    // update quantity
    $update_query = "UPDATE ate 
                     SET quantity = quantity + $add, date = date
                     WHERE username = '$username' AND 
                     SUBSTRING(date, 1, 4) = '$date' AND 
                           foodID = '$foodID'
                    ";
    $update_result = mysql_query($update_query, $dbconnect);

    if ( !$update_result ) {
        die('Invalid Query: ' . mysql_error());
    }

    echo "AFTER UPDATE";
    // Query to Get Eaten Items
    // Copied code from weekley_log.php
    
    $queryAte = "SELECT products.name AS name, ate.foodID AS ID, ate.date AS date, ate.quantity AS quantity FROM ate, products WHERE username = '$username' and ate.foodID = products.foodID";
    $ateResult = mysql_query($queryAte, $dbconnect);

    if ( !$ateResult ) {
        die('Invalid Query: ' . mysql_error());
    }
    echo mysql_fetch_assoc($ateResult);
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
    
    // Close Database Connection
    mysql_free_result($ateResult);
    mysql_close($dbconnect);
?>