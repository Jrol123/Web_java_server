// const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
// const appendAlert = (message, type) => {
//     const wrapper = document.createElement('div')
//     wrapper.innerHTML = [
//         `<div class="alert alert-${type} alert-dismissible" role="alert">`,
//         `   <div>${message}</div>`,
//         '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
//         '</div>'
//     ].join('')
//
//     alertPlaceholder.append(wrapper)
// }

const button_alert = document.getElementById("alertButton");
console.log(button_alert);
function alertTest(){
    alert('Тестовое уведомление');
}
button_alert.onclick = alertTest;