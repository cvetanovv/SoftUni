function addItem() {
    let inputValue = document.getElementById("newItemText").value;
    let itemElement = document.getElementById("items");
    let liElement = document.createElement("li");

    liElement.textContent = inputValue;
    itemElement.appendChild(liElement);
}