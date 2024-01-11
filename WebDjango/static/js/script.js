// const button_alert = document.getElementById("alertButton");
// console.log(button_alert);
// function alertTest(){
//     alert('Тестовое уведомление');
// }
// button_alert.onclick = alertTest;

function subscribe_call() {
    let text = document.getElementById("floatingInput").value;
    let data = new FormData();
    data.append('text', text);
    let validator = /\S+@\S+\.\S+/;
    if (validator.test(text)) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "/save/",
            data: data,
            processData: false,
            contentType: false,
            success: function (response) {
                // Обработка успешного ответа от сервера
                console.log(response);
                // Hide elements on successful response
                document.getElementById("button-inp").style.display = "none";
                document.getElementById("mail-inp").style.display = "none";
                document.getElementById("thx-id").style.display = "block";
            },
            error: function (error) {
                // Обработка ошибки
                console.log(error);
            }
        });
    }
}
function scrollToHeight(height) {
    window.scrollTo({
        top: height,
        behavior: 'smooth' //Добавляет плавность прокрутке
    });
}

function get_result() {
    // получение данных
    let data = new FormData();

    data.append('who', document.getElementById('my-program').value);
    data.append('how_know', document.getElementById('my-form-program').value);

    let types = {1: 'Очень', 2: 'Не совсем', 3: 'Нет'}
    for(let i = 1; i < 4; i++){
        if(document.getElementById('firstRadioDefault' + i.toString()).checked){
            data.append('form', types[i]);
        }
    }

    let answers = []
    for(let i = 1; i < 8; i++){
        if(document.getElementById('flexCheckDefault' + i.toString()).checked){
            answers.push(i);
        }
    }
    data.append('answ', answers);

    $.ajax({
        type: "POST",
        url: "/save_quiz/",
        data: data,
        processData: false,
        contentType: false,
        success: function (response) {
            // Обработка успешного ответа от сервера
            console.log(response);

            $.ajax({
                url: '/statistic/',
                type: 'GET',
                success: function (response) {

                    document.getElementById('answ1').innerHTML = response['who'];
                    document.getElementById('answ2').innerHTML = response['how_know'];
                    document.getElementById('answ3').innerHTML = response['form'];

                    for(let i = 1; i < 8; i++){
                        document.getElementById('result' + i.toString()).value = response['percent'][i - 1].toString();
                        // document.getElementById('result-text' + i.toString()).value = response['percent'][i - 1].toString();
                    }

                    document.getElementById('quiz-block1').style.display = 'none';
                    document.getElementById('quiz-block2').style.display = 'none';
                    document.getElementById('quiz-block3').style.display = 'block';

                    console.log(response);
                }
            });
        },
        error: function (error) {
            // Обработка ошибки
            console.log(error);
        }
    });
}

