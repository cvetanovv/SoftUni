function subtract() {
    const firstNumElement = Number(document.getElementById('firstNumber').value);
    const secondNumElement = Number(document.getElementById('secondNumber').value);

    const resultElement = document.getElementById('result');
    resultElement.textContent = firstNumElement - secondNumElement;
}