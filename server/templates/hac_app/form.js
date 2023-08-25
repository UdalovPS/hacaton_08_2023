console.log('hi from form.js');

document.addEventListener('DOMContentLoaded', function() {
 

    const form = document.getElementById('upload-form');
    const outputDiv = document.getElementById('output');

    form.addEventListener('submit', async function(event) {
        console.log('submit');
        event.preventDefault();

        const formData = new FormData(form);
       
            // console.log(formData.get('textInput'));  //выводит текст из текстового поля формы
            // console.log(formData.get('fileToUpload')); // выводит файл, загруженный в форму
       
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                console.log('response получен');
                const data = await response.json();
                outputDiv.textContent = 'Получен json: ' + JSON.stringify(data, null, 2); // Форматированный вывод JSON
                form.reset(); // Сбрасываем форму

                // ------------ вывод графика ------------
                // let myCanv = document.querySelector('canvas');
                // console.log(myCanv);

                new Chart(document.getElementById("bar-chart-horizontal"), {
                    type: 'horizontalBar',
                    data: {
                        // labels: data.data.labels,
                      labels: ["Санкт-Петербург г., Яхтеная ул., 18 д., 16 к., 4 кв.",
                               "Санкт-Петербург г., Яхтеная ул., 18/16  4 кв.",
                               "СПБ, улица Яхтеная, 18-16-4 к",
                               "Санкт-Петербург, ул. Яхтеная, д. 18, кв. 16-4",
                               "Санкт-Петербург, Яхтеная ул., 18, кв. 16/4"],
                        
                        // datasets: [{
                        //     label: "Предсказание",
                        //     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                        //     data: data.data.datasets[0].data
                        //  }]

                      datasets: [
                        {
                          label: "Предсказание",
                          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                          data: [0.97, 0.02, 0.005, 0.003, 0.001]
                        }
                      ]
                    },
                    options: {
                      legend: { display: false },
                      title: {
                        display: true,
                        text: 'Наиболее вероятные варианты корректировки адресов'
                      }
                    }
                });
                
                // ------------------------------------------

            } else {
                outputDiv.textContent = 'Ошибка при загрузке файла.';
            }
        } catch (error) {
            console.error('Произошла ошибка:', error);
            outputDiv.textContent = 'Произошла ошибка при выполнении запроса.';
        }
        document.getElementById("bar-chart-horizontal").classList.add('canvas_active');
        document.querySelector('.body').classList.add('pb100');
    });
});
