var submitbtn = document.getElementById('submit_btn')
console.log('Script running')

submitbtn.addEventListener("click", async function () {
    console.log("Btn clicked!")
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')
    console.log(csrf_token)

    let email_field = document.getElementById('email_field')
    console.log(email_field.textContent)

    let pass_field = document.getElementById('password_field')
    console.log(pass_field.textContent)

    const data_body = {"csrfmiddlewaretoken": csrf_token[0].value.toString(), "email": email_field.textContent.toString(), "password": pass_field.textContent.toString()}

    await submitForm("http://127.0.0.1:8000/teacher/login/", data_body)
})

async function submitForm(p_url, p_body){
    var xhttp = new XMLHttpRequest()
    xhttp.open("POST", p_url)
    xhttp.send(p_body)
}