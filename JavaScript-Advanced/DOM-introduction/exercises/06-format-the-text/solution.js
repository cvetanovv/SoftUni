function solve() {
  let textArr = document.getElementById('input').value.split('.').filter(x => x.length >= 1)
  let outputElement = document.getElementById('output');

  while (textArr.length > 0){
    let paragraphs = textArr.splice(0, 3).join('.') + '.';
    let text = `<p>${paragraphs}</p>`
    outputElement.innerHTML += text;
  }
}