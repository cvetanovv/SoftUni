function addItem() {
    let inputValue = document.getElementById("newItemText").value;
    let itemElement = document.getElementById("items");
    let liElement = document.createElement("li");

    let deleteLink = document.createElement("a");
    deleteLink.href = "#";
    deleteLink.textContent = "[Delete]";

    liElement.textContent = inputValue;
    itemElement.appendChild(liElement);
    liElement.appendChild(deleteLink);

    deleteLink.addEventListener('click', onDelete);

    function onDelete(event) {
        currentRowElement = event.currentTarget.parentElement;
        currentRowElement.remove();
    }
}