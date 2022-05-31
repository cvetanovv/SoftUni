function search() {
   let townElements = document.querySelectorAll("#towns li");
   let textInput = document.getElementById("searchText").value;
   let resultElement = document.getElementById("result");
   let matches = 0;

   for (let townEl of townElements) {
      let text = townEl.textContent;

      if(text.match(textInput)) {
         matches++
         townEl.style.fontWeight = 'bold';
         townEl.style.textDecoration = 'underline'
      }else {
         townEl.style.fontWeight = 'normal';
         townEl.style.textDecoration = ''
      }
   }

   resultElement.textContent = `${matches} matches found`
}
