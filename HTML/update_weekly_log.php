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
    $foodId = $_GET['id'];
    $date = $_GET['date'];
    $add = intval($_GET['add']);
    // update quantity and delete items with quantity 0
    // date: yyyy-mm-dd
 echo "<h4>TEST1</h4>";
    try {
        echo "<h4>TEST2</h4>";
        $this->pdo->beginTransaction();
        echo "<h4>TEST3</h4>";
        $update_query = "UPDATE ate
                            SET quantity = quantity + $add, date = date
                            WHERE username = '$username' AND
                            DATEDIFF(date, '$date') = 0 AND
                            foodID = '$foodID'";
echo "<h4>TEST4</h4>";
        $delete_query = "DELETE FROM ate
                            WHERE username = '$username' AND
                            DATEDIFF(date, '$date') = 0 AND
                            foodID = '$foodID'
                            AND quantity = 0";
                            echo "<h4>TEST5</h4>";
        $this->pdo->commit();
        echo "<h4>TEST6</h4>";
    } catch(PDOException $e) {
        $this->pdo->rollback();
        echo "<h4>TEST7</h4>";
        die($e->getMessage());
    }


    // $update_query = "UPDATE ate
    //                  SET quantity = quantity + $add, date = date
    //                  WHERE username = '$username' AND
    //                  SUBSTRING(date, 1, 4) = SUBSTRING('$date', 1, 4) AND
    //                  SUBSTRING(date, 6, 2) = SUBSTRING('$date', 6, 2) AND
    //                  SUBSTRING(date, 9, 2) = SUBSTRING('$date', 9, 2) AND
    //                  foodID = '$foodId'
    //                 ";
    // $update_result = mysql_query($update_query, $dbconnect);
    //
    // if ( !$update_result ) {
    //     die('Invalid Query: ' . mysql_error());
    // }

    // delete the item with the quantity 0
    // $delete_query = "DELETE FROM ate
    //                  WHERE username = '$username' AND
    //                  SUBSTRING(date, 1, 4) = SUBSTRING('$date', 1, 4) AND
    //                  SUBSTRING(date, 6, 2) = SUBSTRING('$date', 6, 2) AND
    //                  SUBSTRING(date, 9, 2) = SUBSTRING('$date', 9, 2) AND
    //                  foodID = '$foodId' AND
    //                  quantity = 0
    //                 ";
    //
    // $delete_result = mysql_query($delete_query, $dbconnect);
    // if ( !$delete_result ) {
    //     die('Invalid Query: ' . mysql_error());
    // }


    // Query to Get Eaten Items
    // Copied code from weekley_log.php

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

    // Display Recipes
    $queryRecipes = "SELECT recipes.name AS name, ate.foodID AS ID, ate.date AS date, ate.quantity AS quantity FROM ate, recipes WHERE username = '$username' and ate.foodID = recipes.foodID";
    $recipeResult = mysql_query($queryRecipes, $dbconnect);

    if (!$recipeResult){
        die("Invalid Query:" . mysql_error());
    }
    while ( $row = mysql_fetch_assoc($recipeResult) ) {
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
    mysql_free_result($recipeResult);
    mysql_free_result($update_result);
    mysql_free_result($ateResult);
    mysql_close($dbconnect);
?>
