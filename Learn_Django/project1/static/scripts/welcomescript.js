function get_cookie_dict(cookie_str) {
    let cookie_dict = {}
    let all_cookies = document.cookie.split(';')
    all_cookies.forEach(element => {
        let key_value = element.trim().split('=')
        cookie_dict[key_value[0]] = key_value[1]
    });

    return cookie_dict
}

function check_user_auth(){
    console.log(document.cookie)
    const cookie_dict = get_cookie_dict(document.cookie)
    console.log(cookie_dict)
    const hasToken = "token" in (cookie_dict ? cookie_dict:{});
    if (hasToken){
        console.log('User is already authenticated!')
        document.querySelector('#authed').classList.remove('inactive')
        document.querySelector('#unauth').classList.add('inactive')
    }else{
        console.log('User has not authenticated!')
        document.querySelector('#authed').classList.add('inactive')
        document.querySelector('#unauth').classList.remove('inactive')
    }
}

check_user_auth();

function set_listners(){
    const letsgobtn = document.getElementById('')
}