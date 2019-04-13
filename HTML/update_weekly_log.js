function update_quantity(add, id_and_date) {
    var params = id_and_date.split("&")
    params.push(add.toString())
    console.log(params)
    var jquery_data_str = "username=" + params[0] + 
                          "&id=" + params[1] + 
                          "&date=" + params[2] + 
                          "&add=" + params[3]
    console.log(jquery_data_str)
    
    $.ajax({
        cache: false,
        url: "update_weekly_log.php",
        data: jquery_data_str,
        success: function(data) {
            $("#weekly_log_content").html(data)
        }
    })

    
}

$(document).on('click', ".weekly_log_plus_button",  function(event) {

    console.log(event.target.id)
    update_quantity(1, event.target.id)
 }
);

$(document).on('click', ".weekly_log_minus_button",   function(event) {
    console.log(event.target.id)
    update_quantity(-1, event.target.id)
 }
);

