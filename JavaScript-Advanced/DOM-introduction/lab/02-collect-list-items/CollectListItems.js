function extractText() {
    let itemElements = Array.from(document.querySelectorAll('li'));
    let textAreaElement = document.getElementById('result');
    let valueArr = itemElements.map(e => {
        return e.textContent;
    });
    console.log(valueArr);
    textAreaElement.value = valueArr.join('\n')
}