import get_cookie_dict  from "./utils.js"

var submitbtn = document.getElementById('submit_btn')
console.log('Script running')

submitbtn.addEventListener("click", async function (event) {
    event.preventDefault()
    console.log("Btn clicked!")
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')
    console.log(csrf_token)

    // fetch(url,
    //     {
    //         method: 'GET'
    //     }
    // )
    // .then(response => response.json())
    // .then(
    //     data => {
    //         //
    //     }
    // )

    // console.log(document.cookie)

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
            if (data){
            console.log(data)
            if (data['status']){
                const cookie_dict = get_cookie_dict(document.cookie)
                if (!cookie_dict['token']){
                    document.cookie = `token=${data['data']['token']}; path=/teacher;`
                }
                
                location = 'http://127.0.0.1:8000/teacher/'
                fetch('http://127.0.0.1:8000/teacher/',
                    {
                        method: 'GET',
                        credentials:"include",
                        headers:{
                            'Content-Type': 'application/json',
                            'token': cookie_dict['token']
                        },
                    }
                )
                .then(
                    response => response.json()
                )
                .then(
                    p_data => console.log(p_data)
                )
            }
            }
            else{
                console.log('No response received!')
            }
        }
    )
    .catch(error => console.error('Error:', error));
}