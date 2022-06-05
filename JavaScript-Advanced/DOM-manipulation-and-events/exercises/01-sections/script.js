function create(words) {
   let content = document.getElementById('content');

   words.forEach(word => {
      divElement = document.createElement('div');
      paragraphElement = document.createElement('p');
      paragraphElement.style.display = 'none';
      paragraphElement.textContent = word;

      divElement.appendChild(paragraphElement);
      content.appendChild(divElement);

      divElement.addEventListener('click', onClick);

      function onClick(event) {
         pEl = event.target.querySelectorAll('p')[0];
         console.log(pEl)
         pEl.style.display = 'block';
      }
   })
}