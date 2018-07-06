function x(m) {
	
		var countofo=0;
		var countofx=0;
		var countofp=0;
		

		if(document.getElementById("1").value=="x")
			countofx++;
		else if(document.getElementById("1").value=="o")
			countofo++; 
		else if(document.getElementById("1").value=="+")
			countofp++; 
	
		if(document.getElementById("2").value=="x")
			countofx++;
		else if(document.getElementById("2").value=="o")
			countofo++; 
		else if(document.getElementById("2").value=="+")
			countofp++; 
	
	
		if(document.getElementById("3").value=="x")
			countofx++;
		else if(document.getElementById("3").value=="o")
			countofo++; 
		else if(document.getElementById("3").value=="+")
			countofp++; 
		
	
	
		if(document.getElementById("4").value=="x")
			countofx++;
		else if(document.getElementById("4").value=="o")
			countofo++; 
		else if(document.getElementById("4").value=="+")
			countofp++; 
		
		if(document.getElementById("5").value=="x")
			countofx++;
		else if(document.getElementById("5").value=="o")
			countofo++; 
		else if(document.getElementById("5").value=="+")
			countofp++; 
	
	
		if(document.getElementById("6").value=="x")
			countofx++;
		else if(document.getElementById("6").value=="o")
			countofo++; 
		else if(document.getElementById("6").value=="+")
			countofp++; 
	
	
		if(document.getElementById("7").value=="x")
			countofx++;
		else if(document.getElementById("7").value=="o")
			countofo++; 
		else if(document.getElementById("7").value=="+")
			countofp++; 
	
	
		if(document.getElementById("8").value=="x")
			countofx++;
		else if(document.getElementById("8").value=="o")
			countofo++; 
		else if(document.getElementById("8").value=="+")
			countofp++; 
	
	
		if(document.getElementById("9").value=="x")
			countofx++;
		else if(document.getElementById("9").value=="o")
			countofo++; 
		else if(document.getElementById("9").value=="+")
			countofp++; 

		if(document.getElementById("10").value=="x")
			countofx++;
		else if(document.getElementById("10").value=="o")
			countofo++; 
		else if(document.getElementById("10").value=="+")
			countofp++; 

		if(document.getElementById("11").value=="x")
			countofx++;
		else if(document.getElementById("11").value=="o")
			countofo++; 
		else if(document.getElementById("11").value=="+")
			countofp++; 

		if(document.getElementById("12").value=="x")
			countofx++;
		else if(document.getElementById("12").value=="o")
			countofo++; 
		else if(document.getElementById("12").value=="+")
			countofp++; 

		if(document.getElementById("13").value=="x")
			countofx++;
		else if(document.getElementById("13").value=="o")
			countofo++; 
		else if(document.getElementById("13").value=="+")
			countofp++; 

		if(document.getElementById("14").value=="x")
			countofx++;
		else if(document.getElementById("14").value=="o")
			countofo++; 
		else if(document.getElementById("14").value=="+")
			countofp++; 

		if(document.getElementById("15").value=="x")
			countofx++;
		else if(document.getElementById("15").value=="o")
			countofo++; 
		else if(document.getElementById("15").value=="+")
			countofp++; 

		if(document.getElementById("16").value=="x")
			countofx++;
		else if(document.getElementById("16").value=="o")
			countofo++; 
		else if(document.getElementById("16").value=="+")
			countofp++; 

		if(document.getElementById("17").value=="x")
			countofx++;
		else if(document.getElementById("17").value=="o")
			countofo++; 
		else if(document.getElementById("17").value=="+")
			countofp++; 

		if(document.getElementById("18").value=="x")
			countofx++;
		else if(document.getElementById("18").value=="o")
			countofo++; 
		else if(document.getElementById("18").value=="+")
			countofp++; 

		if(document.getElementById("19").value=="x")
			countofx++;
		else if(document.getElementById("19").value=="o")
			countofo++; 
		else if(document.getElementById("19").value=="+")
			countofp++; 

		if(document.getElementById("20").value=="x")
			countofx++;
		else if(document.getElementById("20").value=="o")
			countofo++; 
		else if(document.getElementById("20").value=="+")
			countofp++; 

		if(document.getElementById("21").value=="x")
			countofx++;
		else if(document.getElementById("21").value=="o")
			countofo++; 
		else if(document.getElementById("21").value=="+")
			countofp++; 

		if(document.getElementById("22").value=="x")
			countofx++;
		else if(document.getElementById("22").value=="o")
			countofo++; 
		else if(document.getElementById("22").value=="+")
			countofp++; 

		if(document.getElementById("23").value=="x")
			countofx++;
		else if(document.getElementById("23").value=="o")
			countofo++; 
		else if(document.getElementById("23").value=="+")
			countofp++; 

		if(document.getElementById("24").value=="x")
			countofx++;
		else if(document.getElementById("24").value=="o")
			countofo++; 
		else if(document.getElementById("24").value=="+")
			countofp++; 

		if(document.getElementById("25").value=="x")
			countofx++;
		else if(document.getElementById("25").value=="o")
			countofo++; 
		else if(document.getElementById("25").value=="+")
			countofp++; 

	
		
var	p=m;
var tot=countofo+countofx+countofp;
var sum=countofx+countofo;


	
	if((countofx==countofo)&&(countofo==countofp))
	{
		document.getElementById(p).value = "x";
		win();

	}
	else if((countofx+countofo+countofp+1)%3==0)
	{
		document.getElementById(p).value = "+";
		win();
	}
	
	else if((countofx+countofo+countofp+2)%3==0) {
		document.getElementById(p).value = "o";
		win();
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
	document.getElementById(10).value = "";
	document.getElementById(11).value = "";
	document.getElementById(12).value = "";
	document.getElementById(13).value = "";
	document.getElementById(14).value = "";
	document.getElementById(15).value = "";
	document.getElementById(16).value = "";
	document.getElementById(17).value = "";
	document.getElementById(18).value = "";
	document.getElementById(19).value = "";
	document.getElementById(20).value = "";
	document.getElementById(21).value = "";
	document.getElementById(22).value = "";
	document.getElementById(23).value = "";
	document.getElementById(24).value = "";
	document.getElementById(25).value = "";
	
	

}
function win()
{
	if(document.getElementById("1").value=="o")
				if(document.getElementById("2").value=="o")
					if(document.getElementById("3").value=="o")
						if(document.getElementById("4").value=="o")
							if(document.getElementById("5").value=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("2").value=="x")
					if(document.getElementById("3").value=="x")
						if(document.getElementById("4").value=="x")
							if(document.getElementById("5").value=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(document.getElementById("1").value=="+")
				if(document.getElementById("2").value=="+")
					if(document.getElementById("3").value=="+")
						if(document.getElementById("4").value=="+")
							if(document.getElementById("5").value=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(document.getElementById("6").value=="o")
				if(document.getElementById("7").value=="o")
					if(document.getElementById("8").value=="o")
						if(document.getElementById("9").value=="o")
							if(document.getElementById("10").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("6").value=="x")
				if(document.getElementById("7").value=="x")
					if(document.getElementById("8").value=="x")
						if(document.getElementById("9").value=="x")
							if(document.getElementById("10").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("6").value=="+")
				if(document.getElementById("7").value=="+")
					if(document.getElementById("8").value=="+")
						if(document.getElementById("9").value=="+")
							if(document.getElementById("10").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("11").value=="o")
				if(document.getElementById("12").value=="o")
					if(document.getElementById("13").value=="o")
						if(document.getElementById("14").value=="o")
							if(document.getElementById("15").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("11").value=="x")
				if(document.getElementById("12").value=="x")
					if(document.getElementById("13").value=="x")
						if(document.getElementById("14").value=="x")
							if(document.getElementById("15").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("11").value=="+")
				if(document.getElementById("12").value=="+")
					if(document.getElementById("13").value=="+")
						if(document.getElementById("14").value=="+")
							if(document.getElementById("15").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("16").value=="o")
				if(document.getElementById("17").value=="o")
					if(document.getElementById("18").value=="o")
						if(document.getElementById("19").value=="o")
							if(document.getElementById("20").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("16").value=="x")
				if(document.getElementById("17").value=="x")
					if(document.getElementById("18").value=="x")
						if(document.getElementById("19").value=="x")
							if(document.getElementById("20").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("16").value=="+")
				if(document.getElementById("17").value=="+")
					if(document.getElementById("18").value=="+")
						if(document.getElementById("19").value=="+")
							if(document.getElementById("20").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("21").value=="o")
				if(document.getElementById("22").value=="o")
					if(document.getElementById("23").value=="o")
						if(document.getElementById("24").value=="o")
							if(document.getElementById("25").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("21").value=="x")
				if(document.getElementById("22").value=="x")
					if(document.getElementById("23").value=="x")
						if(document.getElementById("24").value=="x")
							if(document.getElementById("25").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("21").value=="+")
				if(document.getElementById("22").value=="+")
					if(document.getElementById("23").value=="+")
						if(document.getElementById("24").value=="+")
							if(document.getElementById("25").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("1").value=="o")
				if(document.getElementById("6").value=="o")
					if(document.getElementById("11").value=="o")
						if(document.getElementById("16").value=="o")
							if(document.getElementById("21").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("6").value=="x")
					if(document.getElementById("11").value=="x")
						if(document.getElementById("16").value=="x")
							if(document.getElementById("21").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("1").value=="+")
				if(document.getElementById("6").value=="+")
					if(document.getElementById("11").value=="+")
						if(document.getElementById("16").value=="+")
							if(document.getElementById("21").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("2").value=="o")
				if(document.getElementById("7").value=="o")
					if(document.getElementById("12").value=="o")
						if(document.getElementById("17").value=="o")
							if(document.getElementById("22").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("2").value=="x")
				if(document.getElementById("7").value=="x")
					if(document.getElementById("12").value=="x")
						if(document.getElementById("17").value=="x")
							if(document.getElementById("22").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("2").value=="+")
				if(document.getElementById("7").value=="+")
					if(document.getElementById("12").value=="+")
						if(document.getElementById("17").value=="+")
							if(document.getElementById("22").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("3").value=="o")
				if(document.getElementById("8").value=="o")
					if(document.getElementById("13").value=="o")
						if(document.getElementById("18").value=="o")
							if(document.getElementById("22").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("3").value=="x")
				if(document.getElementById("8").value=="x")
					if(document.getElementById("13").value=="x")
						if(document.getElementById("18").value=="x")
							if(document.getElementById("22").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("3").value=="+")
				if(document.getElementById("8").value=="+")
					if(document.getElementById("13").value=="+")
						if(document.getElementById("18").value=="+")
							if(document.getElementById("22").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("4").value=="o")
				if(document.getElementById("9").value=="o")
					if(document.getElementById("14").value=="o")
						if(document.getElementById("19").value=="o")
							if(document.getElementById("24").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("4").value=="x")
				if(document.getElementById("9").value=="x")
					if(document.getElementById("14").value=="x")
						if(document.getElementById("19").value=="x")
							if(document.getElementById("24").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("4").value=="+")
				if(document.getElementById("9").value=="+")
					if(document.getElementById("14").value=="+")
						if(document.getElementById("19").value=="+")
							if(document.getElementById("24").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("5").value=="o")
				if(document.getElementById("10").value=="o")
					if(document.getElementById("15").value=="o")
						if(document.getElementById("20").value=="o")
							if(document.getElementById("25").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("5").value=="x")
				if(document.getElementById("10").value=="x")
					if(document.getElementById("15").value=="x")
						if(document.getElementById("20").value=="x")
							if(document.getElementById("25").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("5").value=="+")
				if(document.getElementById("10").value=="+")
					if(document.getElementById("15").value=="+")
						if(document.getElementById("20").value=="+")
							if(document.getElementById("25").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("1").value=="o")
				if(document.getElementById("7").value=="o")
					if(document.getElementById("13").value=="o")
						if(document.getElementById("19").value=="o")
							if(document.getElementById("25").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("1").value=="x")
				if(document.getElementById("7").value=="x")
					if(document.getElementById("13").value=="x")
						if(document.getElementById("19").value=="x")
							if(document.getElementById("25").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("1").value=="+")
				if(document.getElementById("7").value=="+")
					if(document.getElementById("13").value=="+")
						if(document.getElementById("19").value=="+")
							if(document.getElementById("25").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		if(document.getElementById("5").value=="o")
				if(document.getElementById("9").value=="o")
					if(document.getElementById("13").value=="o")
						if(document.getElementById("17").value=="o")
							if(document.getElementById("21").value=="o")
					{
						alert("o won Please reset the game.");
					}
		if(document.getElementById("5").value=="x")
				if(document.getElementById("9").value=="x")
					if(document.getElementById("13").value=="x")
						if(document.getElementById("17").value=="x")
							if(document.getElementById("21").value=="x")
					{
						alert("x won Please reset the game.");
					}
		if(document.getElementById("5").value=="+")
				if(document.getElementById("9").value=="+")
					if(document.getElementById("13").value=="+")
						if(document.getElementById("17").value=="+")
							if(document.getElementById("21").value=="+")
					{
						alert("+ won Please reset the game.");
					}
		
		if(tot==24)
		{
			alert("draw Please reset the game.");
		}
}