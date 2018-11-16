function showPass() {
    var pass1 = $("#id_password1");
    var pass2 = $("#id_password2");
    
    if (pass1.attr('type') === "password") {
        pass1.attr('type', 'text');
    } else {
        pass1.attr('type', 'password');
    }
   
    if (pass2.attr('type') === "password") {
        pass2.attr('type', 'text');
    } else {
        pass2.attr('type', 'password');
    }
}

function passMatch() {
    var pass = $("#id_password1").val();
    var confirmPass = $("#id_password2").val();

    if (pass !== confirmPass) {
        $("#checkPassMatch").html("Passwords do not match");
    } else {
        $("#checkPassMatch").html("");
    }
}

$(document).ready(function() {
     $("#id_password1, #id_password2").keyup(passMatch);
});


