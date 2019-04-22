
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

$(document).on("click", "input[name='add_item_button']", function(event) {
    console.log("add item button clickec")    
})
