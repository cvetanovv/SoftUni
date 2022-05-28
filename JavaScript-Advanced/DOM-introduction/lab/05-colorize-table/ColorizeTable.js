function colorize() {
    let rowElements = Array.from(document.querySelectorAll('tr:nth-child(2n)'));
    
    rowElements.forEach(e => console.log(e))
    rowElements.forEach(e => e.style.backgroundColor = "Teal");
}