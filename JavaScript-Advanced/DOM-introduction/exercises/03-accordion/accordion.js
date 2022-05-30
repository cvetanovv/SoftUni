function toggle() {
    let buttonElement = document.getElementsByClassName('button')[0];
    let textElement = document.getElementById('extra');

    // if (buttonElement.textContent = 'More') {
    //     buttonElement.textContent = 'Extra';
    //     textElement.style.display = 'block';
    // } else {
    //     textElement.style.display = '';
    // }
    buttonElement.textContent = buttonElement.textContent === 'less' ? 'more' : 'less';
    textElement.style.display = textElement.style.display === 'block' ? 'none' : 'block';

}