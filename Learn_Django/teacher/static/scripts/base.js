import get_cookie_dict from "./utils.js"
import {get_welcome_page, get_teacher_login_page} from "./apicalls.js";
import { url_teacher_home, url_welcome_page, url_teacher_login_page } from "./urls.js";

const authbtn = document.getElementById('authbtn')
const notifybtn = document.getElementById('notification')

function logoutUser(){
    document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.href = url_teacher_login_page;
}

if (authbtn){

authbtn.addEventListener('click', function () {
    console.log('btn clicked!') 
    const cookie_dict = get_cookie_dict(document.cookie)
    if (!cookie_dict['token']){
        console.log('Logout btn clicked, where user not logged in!')
        window.location.href = url_teacher_login_page;
    }
    
    logoutUser();
})

notifybtn.addEventListener('click', function(){
    

    const panel = document.getElementById("notificationPanel");
    
    if (!panel.classList.contains("active")){
        console.log('Getting notifications.')
        // Getting all notifications
        const url = "http://127.0.0.1:8000/notifications/getnotifications/student/1"

        fetch(url)
        .then(response => response.json())
        .then(
            data => {
                console.log(data)
                const notifiList = document.getElementById('notificationList')
                notifiList.innerHTML = ""
                data.forEach(notification => {
                    const el = document.createElement('li')
                    el.textContent = notification['title']
                    notifiList.appendChild(el)
                });
            }
        )
        .catch(error => console.error('Error:', error));

    }

    panel.classList.toggle("active");
})

}