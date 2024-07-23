const data = null;

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener('readystatechange', function () {
	if (this.readyState === this.DONE) {
		console.log(this.responseText);
	}
});

xhr.open('GET', 'https://euribor.p.rapidapi.com/');
xhr.setRequestHeader('x-rapidapi-key', 'bcd7f52af1msh6fbe910d79df94bp1e7ee4jsne94c78fcd98a');
xhr.setRequestHeader('x-rapidapi-host', 'euribor.p.rapidapi.com');

xhr.send(data);