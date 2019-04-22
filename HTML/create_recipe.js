
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
// each food items is also an array; 0-index: name, 1: food id, 2: quantity, 3: quantity unit
var item_arr = []
// Add the item selected to the right display area
$(document).on("click", '#_add_item_button', function(event) {
    var item = []
    var name_and_id = $("#item_selected_text").html()
    var quantity = $("#recipe_description_input").val()
    console.log(name_and_id, quantity)
/*
    name_and_id = name_and_id.split(";")
    item.push(name_and_id[0])
    item.push(name_and_id[1].slice(1))
    item_arr.push(item)
    console.log(item_arr)
    */
})
