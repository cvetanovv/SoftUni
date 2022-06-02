function deleteByEmail() {
    let rowElements = Array.from(document.querySelectorAll('tbody tr'));
    let resultElement = document.getElementById('result');
    let inputValue = document.getElementsByName("email")[0].value;
    
    let found = false;

    rowElements.forEach(row => {
        email = row.children[1].textContent;
        if (inputValue === email){
            row.remove();
            found = true;
        }
    })
    if (found) {
        resultElement.textContent = "Deleted."
    } else {
        resultElement.textContent = "Not found."
    }
}