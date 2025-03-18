const authbtn = document.getElementById('authbtn')
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