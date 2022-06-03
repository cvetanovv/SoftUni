function solve() {
   let productElements = Array.from(document.getElementsByClassName('product'));
   let textArea = document.querySelector('textarea');
   let checkoutButton = document.getElementsByClassName('checkout')[0];

   let totalMoneyArr = [];
   let productsList = [];

   productElements.forEach(product => {
      let productDetails = product.getElementsByClassName('product-details')[0];
      let productName = productDetails.getElementsByClassName('product-title')[0].textContent;
      let addElement = product.getElementsByClassName('add-product')[0];
      let price = Number(product.getElementsByClassName('product-line-price')[0].textContent).toFixed(2);
      
      addElement.addEventListener('click', () => {
         totalMoneyArr.push(Number(price))
         if (!productsList.includes(productName)){
            productsList.push(productName)
         }
         textArea.textContent += `Added ${productName} for ${price} to the cart.\n`
      })
   })

   checkoutButton.addEventListener('click', () => {
      productElements.forEach(p => {
         let addElement = p.getElementsByClassName('add-product')[0];
         addElement.setAttribute("disabled", "disabled");
      })

      let totalMoney = totalMoneyArr.reduce((total, current) => {
         return total + current
      }, 0);

      textArea.textContent += `You bought ${productsList.join(', ')} for ${totalMoney.toFixed(2)}.`
   })  
}