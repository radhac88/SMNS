function func(m) {
	// body...
	var noofx=0;
	var noofo=0;
	
	
		if (document.getElementById("1").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("1").innerHTML=="o")
			noofo++;

		if (document.getElementById("2").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("2").innerHTML=="o")
			noofo++;

		if (document.getElementById("3").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("3").innerHTML=="o")
			noofo++;

		if (document.getElementById("4").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("4").innerHTML=="o")
			noofo++;

		if (document.getElementById("5").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("5").innerHTML=="o")
			noofo++;
		if (document.getElementById("6").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("6").innerHTML=="o")
			noofo++;
		if (document.getElementById("7").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("7").innerHTML=="o")
			noofo++;
		if (document.getElementById("8").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("8").innerHTML=="o")
			noofo++;
		if (document.getElementById("9").innerHTML=="x")
			noofx++;  
		else if (document.getElementById("9").innerHTML=="o")
			noofo++;
	
	
	
	
	
	
		
		var b=m;
	
	if(noofx===noofo)
		document.getElementById(b).innerHTML="x";
	else
		document.getElementById(b).innerHTML="o";

	if (document.getElementById("1").innerHTML=="x" && document.getElementById("2").innerHTML=="x" && document.getElementById("3").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("1").innerHTML=="o" && document.getElementById("2").innerHTML=="o" && document.getElementById("3").innerHTML=="o")
		alert("o won");
	if (document.getElementById("4").innerHTML=="x" && document.getElementById("5").innerHTML=="x" && document.getElementById("6").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("4").innerHTML=="o" && document.getElementById("5").innerHTML=="o" && document.getElementById("6").innerHTML=="o")
		alert("o won");
		if (document.getElementById("7").innerHTML=="x" && document.getElementById("8").innerHTML=="x" && document.getElementById("9").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("7").innerHTML=="o" && document.getElementById("8").innerHTML=="o" && document.getElementById("9").innerHTML=="o")
		alert("o won");
	if (document.getElementById("1").innerHTML=="x" && document.getElementById("5").innerHTML=="x" && document.getElementById("9").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("1").innerHTML=="o" && document.getElementById("5").innerHTML=="o" && document.getElementById("9").innerHTML=="o")
		alert("o won");
		if (document.getElementById("3").innerHTML=="x" && document.getElementById("5").innerHTML=="x" && document.getElementById("7").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("3").innerHTML=="o" && document.getElementById("5").innerHTML=="o" && document.getElementById("7").innerHTML=="o")
		alert("o won");
	if (document.getElementById("1").innerHTML=="x" && document.getElementById("4").innerHTML=="x" && document.getElementById("7").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("1").innerHTML=="o" && document.getElementById("4").innerHTML=="o" && document.getElementById("7").innerHTML=="o")
		alert("o won");
if (document.getElementById("2").innerHTML=="x" && document.getElementById("5").innerHTML=="x" && document.getElementById("8").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("2").innerHTML=="o" && document.getElementById("5").innerHTML=="o" && document.getElementById("8").innerHTML=="o")
		alert("o won");
if (document.getElementById("3").innerHTML=="x" && document.getElementById("6").innerHTML=="x" && document.getElementById("9").innerHTML=="x")
		alert("x won");
	else if(document.getElementById("3").innerHTML=="o" && document.getElementById("6").innerHTML=="o" && document.getElementById("9").innerHTML=="o")
		alert("o won");

var tot;
tot=nofox+noofo;
if(tot==8)
alert("draw please reset the game")



		
		
		}
		function res(){
			document.getElementById("1").innerHTML="";
			document.getElementById("2").innerHTML="";
			document.getElementById("3").innerHTML="";
			document.getElementById("4").innerHTML="";
			document.getElementById("5").innerHTML="";
			document.getElementById("6").innerHTML="";
			document.getElementById("7").innerHTML="";
			document.getElementById("8").innerHTML="";
			document.getElementById("9").innerHTML="";
		}
