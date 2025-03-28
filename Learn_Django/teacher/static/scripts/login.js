var submitbtn = document.getElementById('submit_btn')
console.log('Script running')

submitbtn.addEventListener("click", async function (event) {
    event.preventDefault()
    console.log("Btn clicked!")
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')
    console.log(csrf_token)

    let email_field = document.getElementsByName('email')
    console.log(email_field)

    let pass_field = document.getElementsByName('password')
    console.log(pass_field.value)

    const data_body = {"csrfmiddlewaretoken": csrf_token[0].value.toString(), "email": email_field[0].value.toString(), "password": pass_field[0].value.toString()}

    await submitForm("http://127.0.0.1:8000/teacher/login/", data_body)
})

async function submitForm(p_url, p_body){
    console.log(p_url)
    fetch(p_url,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({email: p_body['email'], password: p_body['password']})
    })
    .then(response => response.json())
    .then(
        data => {
            console.log(data)
            if (data['status']){
                document.location = 'http://127.0.0.1:8000/teacher/'
            }
        }
    )
    .catch(error => console.error('Error:', error));
}