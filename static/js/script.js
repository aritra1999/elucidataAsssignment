function make_api_call(file_name) {
    console.log("Requesting: ", file_name);
    $("#processing").css({"display": "block"});
    $.ajax({
        url: file_name,
        type: 'GET'
    })
    .done(function (data, status) {
        if(data.verdict === "success"){
            $('#message_success').text(data.message);
            $("#success").css({"display": "block"});
            $("#processing").css({"display": "none"});
        }else{
            $('#message_error').text(data.message);
            $("#error").css({"display": "block"});
            $("#processing").css({"display": "none"});
        }
    })
    .fail(function (data, status) {
        $('#message_error').text("There has been an issue. Please Try again later.");
        $("#error").css({"display": "block"});
        $("#processing").css({"display": "none"});
    });
}