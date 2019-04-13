function update_quantity(add, id_and_date) {
    var params = id_and_date.split("&")
    params.push(add.toString())
    console.log(params)
    var jquery_data_str = "id=" + params[0] + "&date=" + params[1] + "&add=" + params[2]
    console.log(jquery_data_str)
    /*
    $.ajax({
        cache: false,
        url: "update_weekly_log.php",
        data: id,
        success: function(data) {
            $("#weekly_log_content").html(data)
        }
    })
    */
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