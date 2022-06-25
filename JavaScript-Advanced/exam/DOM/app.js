window.addEventListener("load", solve);

function solve() {
	let publishButton = document.getElementById('publish');
	let tableBodyElement = document.getElementById('table-body');
	let sellCarsContainer = document.getElementById('cars-list');

	let makeElement = document.getElementById('make');
	let modelElement = document.getElementById('model');
	let productYearElement = document.getElementById('year');
	let fuelTypeElement = document.getElementById('fuel');
	let originalCostElement = document.getElementById('original-cost');
	let sellingPriceElement = document.getElementById('selling-price');

	let profit = 0;

	publishButton.addEventListener('click', (event) => {
		event.preventDefault();

		let make = makeElement.value;
		let model = modelElement.value;
		let year = productYearElement.value;
		let fuelType = fuelTypeElement.value;
		let originalCost = originalCostElement.value;
		let sellingPrice = sellingPriceElement.value;
		
		if(make === '' || model === '' || year === '' || fuelType === '' || originalCost === '' || sellingPrice === '') {
            return;
        }

		if (Number(originalCost) > Number(sellingPrice)){
			return;
		}

		let trElement = document.createElement('tr');
		trElement.className = "row";
		trElement.innerHTML = `<td>${make}</td>
		<td>${model}</td>
		<td>${year}</td>
		<td>${fuelType}</td>
		<td>${originalCost}</td>
		<td>${sellingPrice}</td>
		<td>
			<button class="action-btn edit">Edit</button>
        	<button class="action-btn sell">Sell</button>
		</td>`
		
		tableBodyElement.appendChild(trElement);

		let editBtn = trElement.querySelector(".edit")
		let sellBtn = trElement.querySelector(".sell")

		makeElement.value = '';
		modelElement.value = '';
		productYearElement.value = '';
		fuelTypeElement.value = '';
		originalCostElement.value = '';
		sellingPriceElement.value = '';

		editBtn.addEventListener('click', (event) => {
			event.preventDefault();

			makeElement.value = make;
			modelElement.value = model;
			productYearElement.value = year;
			fuelTypeElement.value = fuelType;
			originalCostElement.value = originalCost;
			sellingPriceElement.value = sellingPrice;

			trElement.remove();
		})

		sellBtn.addEventListener('click', (event) => {
			event.preventDefault();

			let liElement = document.createElement('li');
			liElement.className = 'each-list';
			liElement.innerHTML = `<span>${make} ${model}</span>
			<span>${year}</span>
			<span>${Number(sellingPrice) - Number(originalCost)}</span>`
			sellCarsContainer.appendChild(liElement);

			profit += Number(sellingPrice) - Number(originalCost);

			let profitElement = document.getElementById('profit');
			profitElement.textContent = `${profit.toFixed(2)}`;

			trElement.remove();		
		})
	})
}
