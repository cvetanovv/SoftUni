function focused() {
    let inputElements = Array.from(document.querySelectorAll("input"));

  inputElements.forEach((input) => {
    input.addEventListener("focus", focusElement);
    input.addEventListener("blur", blurElement);
  });

  function focusElement(event) {
    parentEl = event.target.parentElement;
    parentEl.classList.add("focused");
  }

  function blurElement(event) {
    parentEl = event.target.parentElement;
    parentEl.classList.remove("focused");
  }
}
