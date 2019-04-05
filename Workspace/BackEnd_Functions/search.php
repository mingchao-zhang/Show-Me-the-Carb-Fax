function pc_permute($items, $perms = array())
{
    if (empty($items))
    {
        echo join(' ', $perms) . ' ';
    }
    else
    {
        for ($i = count($items) - 1; $i >= 0; --$i)
        {
            $newitems = $items;
            $newperms = $perms;
            list($foo) = array_splice($newitems, $i, 1);
            array_unshift($newperms, $foo);
            pc_permute($newitems, $newperms);
        }
    }
}

function query_db($dbconnect,$regex,$db_name)
{
    $query = '(SELECT foodId, name FROM ' . $db_name . ' WHERE name LIKE ' . $regex . ' GROUP BY LENGTH(name) LIMIT 5)';
    $result = mysql_query($query, $dbconnect);
    
    return $result;
}

function search_db($query_string)
{
    $query_string = strtolower($query_string);
    $split_string = explode(“ “, $query_string);
    
    $permutations = pc_permute(split_string);
    
    foreach($permutations as $permutation)
    {
        print_r(permutation);
    }
}


