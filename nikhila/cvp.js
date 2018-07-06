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



	
	if(countofx==countofo)
	{
		document.getElementById(p).value = "x";
		var ran=Math.floor((Math.random()*9) + 1); 

		if(document.getElementById(ran).value=="o"||document.getElementById(ran).value=="x")
		{
				var ran1=Math.floor((Math.random()*9) + 1); 
				document.getElementById(ran1).value ="o";
		}
		else
		{
			document.getElementById(ran).value ="o";
		}


		if(document.getElementById("1").value=="o")
				if(document.getElementById("2").value=="o")
					if(document.getElementById("3").value=="o")
					{	
						alert(" o win Please reset the game.");
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("2").value=="x")
					if(document.getElementById("3").value=="x")
					{	
						alert(" x win Please reset the game.");
					}
		if(document.getElementById("4").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("6").value=="o")
					{
						alert("o win Please reset the game.");
					}
		if(document.getElementById("4").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("6").value=="x")
					{
						alert("x win Please reset the game.");
					}
		if(document.getElementById("7").value=="o")
				if(document.getElementById("8").value=="o")
					if(document.getElementById("9").value=="o")
					{
						alert("o win Please reset the game.");
					}
		if(document.getElementById("7").value=="x")
				if(document.getElementById("8").value=="x")
					if(document.getElementById("9").value=="x")
					{
						alert("x win Please reset the game.");
					}
		if(document.getElementById("1").value=="o")
				if(document.getElementById("4").value=="o")
					if(document.getElementById("7").value=="o")
					{
						alert("o win Please reset the game.");
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("4").value=="x")
					if(document.getElementById("7").value=="x")
					{
						alert("x win Please reset the game.");
					}
		if(document.getElementById("2").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("8").value=="o")
					{
						alert("o win Please reset the game.");
					}
		if(document.getElementById("2").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("8").value=="x")
					{
						alert(" x win Please reset the game.");
					}
		if(document.getElementById("3").value=="o")
				if(document.getElementById("6").value=="o")
					if(document.getElementById("9").value=="o")
					{
						alert("o win Please reset the game.");
					}
		if(document.getElementById("3").value=="x")
				if(document.getElementById("6").value=="x")
					if(document.getElementById("9").value=="x")
					{
						alert("x win Please reset the game.");
					}
		if(document.getElementById("1").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("9").value=="o")
					{
						alert("o win Please reset the game.");
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("9").value=="x")
					{
						alert("x win Please reset the game.");
					}
		if(document.getElementById("3").value=="o")
				if(document.getElementById("5").value=="o")
					if(document.getElementById("7").value=="o")
					{
						alert("o win Please reset the game.");
					}
		if(document.getElementById("3").value=="x")
				if(document.getElementById("5").value=="x")
					if(document.getElementById("7").value=="x")
					{
						alert("x win Please reset the game.");
					}
		if(tot==8)
		{
			alert("draw Please reset the game.");
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
}