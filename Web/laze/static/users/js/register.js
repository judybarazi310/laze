function showPass() {
    var pass1 = $("#id_password1");
    var pass2 = $("#id_password2");
    passType(pass1)
    passType(pass2)
}

function passType(pass){
    if (pass.attr('type') === "password") {
        pass.attr('type', 'text');
    } else {
        pass.attr('type', 'password');
    }
    return pass
}

function passMatch() {
    var pass = $("#id_password1").val();
    var confirmPass = $("#id_password2").val();

    if (confirmPass !== "" && pass !== confirmPass) {
        $("#checkPassMatch").html("Passwords do not match");
}}

$(document).ready(function() {
     $("#id_password1, #id_password2").keyup(passMatch);
});


