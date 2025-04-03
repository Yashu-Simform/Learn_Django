import get_cookie_dict  from "./utils.js"
export {get_welcome_page, teacher_home, get_teacher_login_page};

function get_token(){
    const cookie_dict = get_cookie_dict(document.cookie)
    if (cookie_dict['token']){
        return cookie_dict['token'];
    }

    return null;
}

function teacher_home(p_url){
    token = get_token()
    fetch(p_url,{
        method: 'GET',
        headers:{
            'Content-Type': 'application/json',
            'token': token ? token : ""
        }
    })
    .then()
}

function get_welcome_page(p_url){
    fetch(p_url,{
        method: 'GET',
    })
    .then(
        response => response.json()
    )
    .then(
        data => console.log(data)
    )
}

function get_teacher_login_page(p_url){
    fetch(p_url,{
        method: 'GET',
    })
    .then(
        response => console.log(response)
    )
    .then(
        data => console.log(data)
    )
}