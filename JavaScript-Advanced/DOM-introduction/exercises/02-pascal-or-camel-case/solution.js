function solve() {
  const textElement = document.getElementById('text');
  const namingConventionElement = document.getElementById('naming-convention');
  const resultElement = document.getElementById('result');

  let textArr = textElement.value.split(" ");
  let result = [];

  if (namingConventionElement.value === "Camel Case") {
    let firstWord = textArr[0].toLowerCase();
    result.push(firstWord)
    for (let index = 1; index < textArr.length; index++) {
      let word = textArr[index].toLowerCase();
      let wordCapitalized = word.charAt(0).toUpperCase() + word.slice(1);
      result.push(wordCapitalized);
    }
    resultElement.textContent = result.join('');

  } else if (namingConventionElement.value === "Pascal Case") {
    for (let index = 0; index < textArr.length; index++) {
      let word = textArr[index].toLowerCase();
      let wordCapitalized = word.charAt(0).toUpperCase() + word.slice(1);
      result.push(wordCapitalized);
    }
    resultElement.textContent = result.join('');

  } else {
    resultElement.textContent = 'Error!';
  }
}