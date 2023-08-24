console.log('hi from form.js');

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const outputDiv = document.getElementById('output');

    form.addEventListener('submit', async function(event) {
        console.log('submit');
        event.preventDefault();

        const formData = new FormData(form);
       
            console.log(formData.get('textInput'));  //выводит текст из текстового поля формы
            console.log(formData.get('fileToUpload')); // выводит файл, загруженный в форму
       

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                console.log('response получен');
                const data = await response.json();
                // console.log(data.data);
                // outputDiv.textContent = data.data[0].address;
               
                outputDiv.textContent = JSON.stringify(data, null, 2); // Форматированный вывод JSON
                form.reset(); // Сбрасываем форму

            } else {
                outputDiv.textContent = 'Ошибка при загрузке файла.';
            }
        } catch (error) {
            console.error('Произошла ошибка:', error);
            outputDiv.textContent = 'Произошла ошибка при выполнении запроса.';
        }
    });
});
