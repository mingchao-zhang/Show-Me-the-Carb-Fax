
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
    console.log("clicked")
    console.log(event.target)
    console.log(event.target[0].innerHTML)
    div_elem = "";
    if event.target.id === "" {
        div_elem = event.target.parentNode.id
    }
    else {
        div_elem = event.target.id
    }
    console.log(div_elem, "hello")
    arr = event.target.id.split("&") || event.target[0].innerHTML
    console.log(arr)    
})
