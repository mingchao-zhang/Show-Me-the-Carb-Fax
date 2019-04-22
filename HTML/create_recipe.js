
function search_food() {
    var search_option = "product";
    if ( document.getElementById('_recipe').checked ) {
        search_option = "recipe";               
    }
    var search_name = $("#food_search").val();
    $.ajax({
        cache: false,
        url: "food_search.php",
        data: "name=" + search_name + "&option=" + search_option,
        success: function(data) {
            $("#food_suggestion").html(data);
        }
    })
}         
$("#food_search").bind("keyup mouseenter", search_food);
$('input[name="search_option"]').on('click change', search_food);

// Display the item selected
$(document).on("click", ".food_search_item", function(event) {
    div_elem = "";
    if (event.target.id === "") {
        div_elem = event.target.parentNode.id
    }
    else {
        div_elem = event.target.id
    }
    param_arr = div_elem.split("*")
    item_name = param_arr[0]
    item_id = param_arr[1]
    $("#item_selected_text").html(item_name.replace(/_/g, " ") + "; " + item_id.replace(/_/g, " "))
})

// item_arr stores food items
// each food item is also an array; 0-index: name, 1: food id, 2: quantity, 3: quantity unit, 4: recipe description
// all values in each food item are strings
var item_arr = []
// Add the item selected to the right display area
$(document).on("click", '#_add_item_button', function(event) {
    var item = []

    var name_and_id = $("#item_selected_text").html()
    if ( !name_and_id ) {
        return
    }
    name_and_id = name_and_id.split(";")
    item.push(name_and_id[0])
    item.push(name_and_id[1].slice(1))

    var quantity = $("#quantity_input").val()
    if ( !quantity ) {
        return
    }
    item.push(quantity)

    var quantity_unit = "measurement_std"
    if ( document.getElementById("_volume").checked ) {
        quantity_unit = "volume"    
    }
    else if ( document.getElementById("_weight").checked ) {
        quantity_unit = "weight"    
    }
    item.push(quantity_unit)

    var recipe_description = $("#recipe_description_input").val() || "None"
    item.push(recipe_description)

   
    item_arr.push(item)
    console.log(item_arr)
})
