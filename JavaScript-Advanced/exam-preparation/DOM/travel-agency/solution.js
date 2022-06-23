window.addEventListener('load', solution);

function solution() {
	let submitButton = document.getElementById('submitBTN');
	let editButton = document.getElementById('editBTN');
	let continueButton = document.getElementById('continueBTN');

	let blockEl = document.getElementById('block');
	let previewElement = document.getElementById('infoPreview');

	let fullNameElement = document.getElementById('fname');
	let emailElement = document.getElementById('email');
	let phoneNumberElement = document.getElementById('phone');
	let addressElement = document.getElementById('address');
	let postalCodeElement = document.getElementById('code');

	submitButton.addEventListener('click', () =>{
		let fullName = fullNameElement.value;
		let email = emailElement.value;
		let phoneNumber = phoneNumberElement.value;
		let address = addressElement.value;
		let postalCode = postalCodeElement.value;

		if (fullName === '' || email === '') {
			return;
		}

		submitButton.disabled = true;
		editButton.disabled = false;
		continueButton.disabled = false;

		let previewContainerEl = document.createElement('li');
		previewContainerEl.innerHTML = `<li>Full Name: ${fullName}</li>
		<li>Email: ${email}</li>
		<li>Phone Number: ${phoneNumber}</li>
		<li>Address: ${address}</li>
		<li>Postal Code: ${postalCode}</li>`

		previewElement.appendChild(previewContainerEl);

		fullNameElement.value = '';
		emailElement.value = '';
		phoneNumberElement.value = '';
		addressElement.value = '';
		postalCodeElement.value = '';

		editButton.addEventListener('click', () => {
			fullNameElement.value = fullName;
			emailElement.value = email;
			phoneNumberElement.value = phoneNumber;
			addressElement.value = address;
			postalCodeElement.value = postalCode;

			previewContainerEl.innerHTML = '';
			submitButton.disabled = false;
			editButton.disabled = true;
			continueButton.disabled = true;
			previewContainerEl.remove();
		})

		continueButton.addEventListener('click', () => {
			blockEl.innerHTML = `<h3>Thank you for your reservation!</h3>`
		})
	}) 
}
