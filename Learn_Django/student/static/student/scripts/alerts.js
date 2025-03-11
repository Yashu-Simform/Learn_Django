var messages = document.querySelectorAll('.django-messages')
// var messages = data_container.children
console.log(messages)

console.log('Inside the script!')
for (let index = 0; index < messages.length; index++) {
    const element = messages[index];
    console.log(element.textContent)
    alert(element.textContent)
}
