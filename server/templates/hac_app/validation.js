console.log('validation.js');

let inputs = document.querySelectorAll('input');
console.log(inputs[1].value);

const inputText = inputs[0];
const inputFile = inputs[1];
const button = inputs[2];

inputText.addEventListener('input', e => {
    console.log(inputText.value);
});

button.addEventListener('click', e => {
    e.preventDefault();
    console.log(inputText.value.trim());
    console.log(inputFile.name);
})