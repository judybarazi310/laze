function passMatch() {
    var pass = $("#id_password1").val();
    var confirmPass = $("#id_password2").val();

    if (pass !== confirmPass)
        $("#checkPassMatch").html("Passwords do not match");
    else
        $("#checkPassMatch").html("Passwords match");
        
    console.log(pass);
    console.log(confirmPass);
}

$(document).ready(function() {
     $("#id_password1, #id_password2").keyup(passMatch);
});

