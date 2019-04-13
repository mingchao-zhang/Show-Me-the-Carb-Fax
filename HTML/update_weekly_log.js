function update_quantity(add, id) {
    console.log(id)
    if (add) {
        console.log("increase the quantity by one???")
        id += "&increase=true"
    }
    else {
        console.log("decrease the quantity by one")
        id += "&increase=false"
    }
    console.log(id)
    $.ajax({
        cache: false,
        url: "update_weekly_log.php",
        data: id,
        success: function(data) {
            $("#weekly_log_content").html(data)
        }
    })
}

$(".weekly_log_plus_button").on( "click", function(event) {
    console.log(event.target.id)
    update_quantity(true, event.target.id)
 }
);

$(".weekly_log_minus_button").on( "click", function(event) {
    console.log(event.target.id)
    update_quantity(false, event.target.id)
 }
);