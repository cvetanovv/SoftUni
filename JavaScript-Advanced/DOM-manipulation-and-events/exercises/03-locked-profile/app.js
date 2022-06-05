function lockedProfile() {
    let buttonElement = Array.from(document.querySelectorAll('.profile button'));
    buttonElement.forEach(b => b.addEventListener('click', onClick))


    function onClick(event){
        let profile = event.target.parentElement;
        isUnlock = profile.querySelector('input[value="unlock"]').checked;
        button = event.target
        hiddenElement = Array.from(profile.querySelectorAll('div'))
        .find(p => p.id.includes("HiddenFields"))

        if (isUnlock) {
            if (button.textContent === "Show more"){
                button.textContent = "Hide it";
                hiddenElement.style.display = 'block';
            } else {
                button.textContent = "Show more";
                hiddenElement.style.display = 'none';
            }

        }
    }
}