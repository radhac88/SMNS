function myFunction(){
document.getElementById("demo").innerHTML = "hello";
document.getElementById("demo1").innerHTML =
person.firstName + "  " + person.lastName + "and my phone number is  " + person.phoneNum + "email id =" + person.emailId;
document.getElementById("demo2").innerHTML = x;
var elem = document.getElementById("demo3");
elem.innerHTML = y;
}

var person = {
	firstName : "shiva prasad",
	lastName : "D",
	phoneNum : 9703030365,
	emailId : "shivaprasad.doredla@gmail.com",
	fullName : function(){
		return this.firstName + " " + this.lastName;
	}	
}
var person1 = {
	firstName : "shiva",
	lastName : "D",
}
var x =person.fullName.apply(person1);

y=5;
var y;

function myFunction1() {
	var message, z;
	message = document.getElementById("p01");
	message.innerHTML = "";
	z = document.getElementById("demo4").value;
	try {
	if (z == "") throw "empty";
	if(isNaN(z)) throw "not a number";
	z = Number(z);
	if(z < 5) throw "too low";
	if(z >10) throw "too high";
	//if(z > 5 && z<10) "number entered between 5 and 10";
	}
	catch(err) {
	message.innerHTML = "input is " + err;
	}
	finally {
		document.getElementById("demo4").value ="";
	}
}

function regExp(){
	var x, str;
	str = "visit w3schools";
	x = str.search("schools");
	document.getElementById("demo5").innerHTML = x;

}
var arr = [100,1,5,6,33,22,25];

function sortArray() {
	document.getElementById("demo6").innerHTML = arr.sort(function(a , b){
		return a - b; 
	});
	document.getElementById("demo5").innerHTML = arr[0];
}
function arrRandom() {
	document.getElementById("demo7").innerHTML = arr.sort(function(a , b){
		return 0.5 - Math.random();
	})

}
var day;
function switch1() {
	switch(new Date().getDay()){
		case 0:
		day = "Sunday";
		break;
		case 1:
		day = "monday";
		break;
	}
	document.getElementById("demo8").innerHTML = "Today is " + day;
}
function loops(){
var cars =["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];
var text = "";
var i;
for (var i = 0; i < cars.length; i++) {
	text += cars[i] + "<br>";
}
document.getElementById("demo9").innerHTML = text;
}

