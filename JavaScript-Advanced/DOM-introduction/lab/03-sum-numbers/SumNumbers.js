function calc() {
    const firstNumElement = document.getElementById('num1').value;
    const secondNumElement = document.getElementById('num2').value;
    let resultElement = document.getElementById('sum');

    let result = Number(firstNumElement) + Number(secondNumElement);

    resultElement.value = result;
}
