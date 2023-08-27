// Этот скрипт загружает и хедер и содержимое - из html-файлов.
// Поэтому хедер здесь с css-стилями
// Данный скрипт надо подключить в файле index.html (сейчас там мб подключен другой скрипт)


console.log('hi from script.js');

// Получаем div-ы с хедером и контентом
const contentDiv = document.getElementById('content');
const header = document.querySelector('.global-header');

// Ждем загрузки окна
window.addEventListener('load', (e) => {
    fetch('/header.html') // Запрашиваем  файл с html-кодом хедера
        .then(response => response.text())
        .then(data => {
            // console.log(data);
            header.innerHTML = data; // Выгружаем хедер на страницу

            //После формирования хедера вешаем addEventListener-click на все ссылки в меню хедера
            let links = document.querySelectorAll('.nav a');
            // console.log(links);
            document.querySelector('.nav').addEventListener('click', (event) => {
                // console.log(event.target);
                if (event.target.tagName === 'A') {
                    event.preventDefault();
                    const url = event.target.href;
                    links.forEach(el => {
                        el.classList.remove('active');
                    });
                    event.target.classList.add('active');

                    // history.pushState(null, '', target); // Изменяем URL без перезагрузки
                    loadPage(url);
                }
            });
        })
        .catch(error => {
            console.log('Error loading header.html');
        });

    // Загружаем содержимое файла main.html в див content - для отображения на главной странице 
    fetch('/main.html')
        .then(response => response.text())
        .then(data => {
            // Обработка полученных данных
            // console.log(data);
            contentDiv.innerHTML = data;
        })
        .catch(error => {
            console.error('Error fetching file:', error);
        });    
});


// Функция для загрузки и отображения содержимого HTML-файлов
function loadPage(url) {
    fetch(url)
        .then(response => response.text())
        .then(data => {
            contentDiv.innerHTML = data;
        })
        .catch(error => {
            console.error('Error fetching page:', error);
        });
}