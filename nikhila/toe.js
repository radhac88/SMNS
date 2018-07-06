function x(m) {
	
		var countofo=0;
		var countofx=0;
		

		if(document.getElementById("1").value=="x")
			countofx++;
		else if(document.getElementById("1").value=="o")
			countofo++; 
	
		if(document.getElementById("2").value=="x")
			countofx++;
		else if(document.getElementById("2").value=="o")
			countofo++; 
	
	
		if(document.getElementById("3").value=="x")
			countofx++;
		else if(document.getElementById("3").value=="o")
			countofo++; 
	
	
		if(document.getElementById("4").value=="x")
			countofx++;
		else if(document.getElementById("4").value=="o")
			countofo++; 
		
		if(document.getElementById("5").value=="x")
			countofx++;
		else if(document.getElementById("5").value=="o")
			countofo++; 
	
	
		if(document.getElementById("6").value=="x")
			countofx++;
		else if(document.getElementById("6").value=="o")
			countofo++; 
	
	
		if(document.getElementById("7").value=="x")
			countofx++;
		else if(document.getElementById("7").value=="o")
			countofo++; 
	
	
		if(document.getElementById("8").value=="x")
			countofx++;
		else if(document.getElementById("8").value=="o")
			countofo++; 
	
	
		if(document.getElementById("9").value=="x")
			countofx++;
		else if(document.getElementById("9").value=="o")
			countofo++; 
	
		
var	p=m;
var tot=countofo+countofx;



	
	if(countofx===countofo)
	{
		document.getElementById(p).value = "x";
		win();
		if(tot==8)
		{
			document.getElementById("demo").innerHTML= "draw Please reset the game.";
		}

	}
		
	
	else{
		document.getElementById(p).value = "o";
		win();
		if(tot==8)
		{
			document.getElementById("demo").innerHTML= "draw Please reset the game.";
		}
	}
}

			
function re()
{
	document.getElementById(1).value = "";
	document.getElementById(2).value = "";
	document.getElementById(3).value = "";
	document.getElementById(4).value = "";
	document.getElementById(5).value = "";
	document.getElementById(6).value = "";
	document.getElementById(7).value = "";
	document.getElementById(8).value = "";
	document.getElementById(9).value = "";
	document.getElementById(1).style.background ="" ;
	document.getElementById(2).style.background ="" ;
	document.getElementById(3).style.background ="" ;
	document.getElementById(4).style.background ="" ;
	document.getElementById(5).style.background ="" ;
	document.getElementById(6).style.background ="" ;
	document.getElementById(7).style.background ="" ;
	document.getElementById(8).style.background ="" ;
	document.getElementById(9).style.background ="" ;
	document.getElementById("demo").innerHTML="";
}
function win()
{
	if(document.getElementById("1").value=="o")
				if(document.getElementById("2").value=="o")
					if(document.getElementById("3").value=="o")
					{	
						col(1,2,3);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("2").value=="x")
					if(document.getElementById("3").value=="x")
					{	
						col(1,2,3);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(document.getElementById("4").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("6").value=="o")
					{
						col(4,5,6);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("4").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("6").value=="x")
					{
						col(4,5,6);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(document.getElementById("7").value=="o")
				if(document.getElementById("8").value=="o")
					if(document.getElementById("9").value=="o")
					{
						col(7,8,9);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("7").value=="x")
				if(document.getElementById("8").value=="x")
					if(document.getElementById("9").value=="x")
					{
						col(7,8,9);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(document.getElementById("1").value=="o")
				if(document.getElementById("4").value=="o")
					if(document.getElementById("7").value=="o")
					{
						col(1,4,7);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("4").value=="x")
					if(document.getElementById("7").value=="x")
					{
						col(1,4,7);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(document.getElementById("2").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("8").value=="o")
					{
						col(2,5,8);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("2").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("8").value=="x")
					{
						col(2,5,8);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(document.getElementById("3").value=="o")
				if(document.getElementById("6").value=="o")
					if(document.getElementById("9").value=="o")
					{
						col(3,6,9);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("3").value=="x")
				if(document.getElementById("6").value=="x")
					if(document.getElementById("9").value=="x")
					{
						col(3,6,9);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(document.getElementById("1").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("9").value=="o")
					{
						col(1,5,9);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("9").value=="x")
					{
						col(1,5,9);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(document.getElementById("3").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("7").value=="o")
					{
						col(3,5,7);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(document.getElementById("3").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("7").value=="x")
					{
						col(3,5,7);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		
}
function col(x,y,z)
{
	var p=x;
	var q=y;
	var r=z;
	document.getElementById(p).style.background = "green";
	document.getElementById(q).style.background = "green";
	document.getElementById(r).style.background = "green";
}