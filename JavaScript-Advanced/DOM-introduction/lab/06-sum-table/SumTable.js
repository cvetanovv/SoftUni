function sumTable() {
    let rowsElements = Array.from(document.querySelectorAll('tr')).slice(1, -1);
    let totalElement = document.getElementById('sum')

    sum = 0

    let rowsValue = rowsElements.map(e => {
        let currentNum =  Number(e.lastElementChild.textContent);
        sum += currentNum;
    })
    
    totalElement.textContent = sum;
}