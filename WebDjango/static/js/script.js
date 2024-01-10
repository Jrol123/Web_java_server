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
function set_size(){
    let flag1 = false;
    let flag2 = false;
    if(document.getElementById('quiz-block1').style.display == 'none'){
        document.getElementById('quiz-block1').style.display = 'block';
        flag1 = true;
    }
    if(document.getElementById('quiz-block3').style.display == 'none'){
        document.getElementById('quiz-block3').style.display = 'block';
        flag2 = true;
    }
    let my_height = document.getElementById('sub-block3').clientHeight;
    let my_width = document.getElementById('sub-block3').clientWidth;

    document.getElementById('sub-block1').style.height = my_height.toString() + 'px';
    document.getElementById('sub-block2').style.height = my_height.toString() + 'px';

    document.getElementById('quiz-block3').style.height = document.getElementById('quiz-block1').clientHeight.toString() + 'px';

    document.getElementById('sub-block1').style.width = my_width.toString() + 'px';
    document.getElementById('sub-block2').style.width = my_width.toString() + 'px';
    if(flag1){
        document.getElementById('quiz-block1').style.display = 'none';
    }
    if(flag2){
        document.getElementById('quiz-block3').style.display = 'none';
    }
}
function get_result() {
    // получение данных
    let data = new FormData();

    data.append('program', document.getElementById('my-program').value);
    data.append('type', document.getElementById('my-form-program').value);

    let types = {1: 'очно', 2: 'заочно', 3: 'очно-заочно'}
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

                    document.getElementById('answ1').innerHTML = response['school'];
                    document.getElementById('answ2').innerHTML = response['type'];
                    document.getElementById('answ3').innerHTML = response['form'];

                    for(let i = 1; i < 8; i++){
                        document.getElementById('result' + i.toString()).value = response['percent'][i - 1].toString() + '%';
                    }

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

