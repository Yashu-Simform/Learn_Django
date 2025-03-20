const authbtn = document.getElementById('authbtn')
const notifybtn = document.getElementById('notification')
// let data = JSON.parse("{{ loggedin | escapejs }}")
let data = document.currentScript.getAttribute('loggedin')
console.log(data)

authbtn.addEventListener('click', function () {
    console.log('btn clicked!') 
    if(data == "True"){
        // User has logged in
        const xhttp = new XMLHttpRequest()
        xhttp.open("GET", 'http://127.0.0.1:8000/teacher/logout/')
        xhttp.send()
        console.log(xhttp.response)
    }else{
        // User has not logged in
    }
})

notifybtn.addEventListener('click', function(){
    

    const panel = document.getElementById("notificationPanel");
    
    if (!panel.classList.contains("active")){
        console.log('Getting notifications.')
        // Getting all notifications
        const url = "http://127.0.0.1:8000/notifications/getnotifications/student/1"
        // const xhttp = new XMLHttpRequest()
        // xhttp.open("GET", url)
        // xhttp.send()
        // response = xhttp.responseText
        // console.log(response)

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

