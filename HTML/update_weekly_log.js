function update_quantity(add) {
    console.log("hello???")
    if (add) {
        console.log("increase the quantity by one");
    }
    else {
        console.log("decrease the quantity by one");
    }
}

$(".weekly_log_plus_button").on( "click", function() {
    update_quantity(true)
 }
);

$(".weekly_log_minus_button").on( "click", function() {
    update_quantity(false)
 }
);