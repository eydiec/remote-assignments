const btnUpdate = document.querySelector('.col');
const headline = document.querySelector('h1');
const btn = document.querySelector('.col2')
const action = document.querySelector('.action')


btnUpdate.addEventListener('click',()=>{
	headline.textContent = "Have a Good Time!";
	headline.style.transition= 'font-size 0.6s ease-in-out';
	headline.style.fontSize= '60px'
})

action.addEventListener('click',()=>{
	
	if(btn.style.display=== ''){
		action.textContent = 'View Less';
		action.style.textAlign='center';
		action.style.color='#fff';
		btn.style.display = 'block';
		headline.style.fontSize = '40px';
		headline.style.transition= 'font-size 0.6s ease-in-out';
	}else{
		
		action.textContent = 'View More';
		action.style.textAlign='center';
		action.style.color='#fff';
		action.style.fontFamily='sans-serif';
		btn.removeAttribute('style'); //remove current disply property
		headline.removeAttribute('style');
		headline.style.transition= 'font-size 0.6s ease-in-out';


	}


})