const loginForm = document.getElementById("loginForm")

loginForm.addEventListener("submit",trys)

function trys (){
    let form_data = new FormData(loginForm)
    let objectData = Object.fromEntries(form_data)
    let j_data = JSON.stringify(objectData)
    $.ajax({
        url: "http://127.0.0.1:8000/api/login",
        type: "POST",
        contentType: 'application/json',
        data: j_data,
        success: function(response) {
            console.log(response);
        },
        error: function(xhr, status, error) {
            console.log("Error:", error);
        }
        });
    }