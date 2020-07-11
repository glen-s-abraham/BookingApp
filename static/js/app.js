/*const navMenu=()=>
{
	console.log("app started");
	document.querySelector('.header__menu_btn').addEventListener('click',()=>{
		document.querySelector('.header__menu_btn').classList.toggle('hide');
		document.querySelector('.header__menu_btn').classList.toggle('rotate');

	});
	
}
navMenu();*/

const viewControl=(()=>{
	const elements={
		navbtn:document.querySelector('.header__menu_btn'),
		navmenu:document.querySelector('.header__menu'),
		datefield:document.querySelector('#date'),
		dateForm:document.querySelector('#dateForm')

	};
	return{
		navbtnClick:()=>{
			console.log(elements.navmenu);
			console.log(elements.navbtn);
		    elements.navmenu.classList.toggle('hide');
		    elements.navbtn.classList.toggle('rotate');
		    

		},
		

		getNavbtn:()=>{
			return elements.navbtn;
		},
		
		
	}

}
)();


const appControl=((viewCntrl)=>{
	function startListener(){
		const btn=viewCntrl.getNavbtn();
		
		btn.addEventListener('click',()=>{
			console.log("clicked");
			viewCntrl.navbtnClick();
		});
		
	};
	return{
		init:()=>{
			console.log("appControl started");
			startListener();
		}
	}
})(viewControl);
appControl.init();