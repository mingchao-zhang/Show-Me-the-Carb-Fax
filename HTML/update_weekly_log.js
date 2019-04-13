function update_quantity(add, id) {
    console.log(id)
    if (add) {
        console.log("increase the quantity by one???");
    }
    else {
        console.log("decrease the quantity by one");
    }
}

$(".weekly_log_plus_button").on( "click", function(event) {
    update_quantity(true, event.target.id)
 }
);

$(".weekly_log_minus_button").on( "click", function(event) {
    update_quantity(false, event.target.id)
 }
);