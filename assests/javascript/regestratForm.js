$(document).ready(function(){
    $("#submit").click( function(){
        var name =  $("#name"). val();
        var id  = $("#id").val;
        var password = $("#Pass").val();
        var course = $("#courses").val();
        var sem = $("#semester").val();
        var profile = $("#pro").val();

        if(name == '' || id == '' || password == '' || course == '' || sem == '' || profile == ''){
            swal({
                title: "Field Empty",
                text: "Please Filled All The Feild ",
                icon: "Warning",
                button: "ok",
              });
        }
    })
})