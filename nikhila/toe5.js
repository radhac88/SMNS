function x(m) {
	
		var countofo=0;
		var countofx=0;
		var countofp=0;
	var b1=document.getElementById(1).value; 
	var b2=document.getElementById(2).value ;
	var b3=document.getElementById(3).value ;
	var b4=document.getElementById(4).value ;
	var b5=document.getElementById(5).value ;
	var b6=document.getElementById(6).value ;
	var b7=document.getElementById(7).value ;
	var b8=document.getElementById(8).value ;
	var b9=document.getElementById(9).value ;
	var b10=document.getElementById(10).value ;
	var b11=document.getElementById(11).value ;
	var b12=document.getElementById(12).value ;
	var b13=document.getElementById(13).value ;
	var b14=document.getElementById(14).value ;
	var b15=document.getElementById(15).value ;
	var b16=document.getElementById(16).value ;
	var b17=document.getElementById(17).value ;
	var b18=document.getElementById(18).value ;
	var b19=document.getElementById(19).value ;
	var b20=document.getElementById(20).value ;
	var b21=document.getElementById(21).value ;
	var b22=document.getElementById(22).value ;
	var b23=document.getElementById(23).value ;
	var b24=document.getElementById(24).value ;
	var b25=document.getElementById(25).value ;
	
	

		if(b1=="x")
			countofx++;
		else if(b1=="o")
			countofo++; 
		else if(b1=="+")
			countofp++; 
	
		if(b2=="x")
			countofx++;
		else if(b2=="o")
			countofo++; 
		else if(b2=="+")
			countofp++; 
	
	
		if(b3=="x")
			countofx++;
		else if(b3=="o")
			countofo++; 
		else if(b3=="+")
			countofp++; 
		
	
	
		if(b4=="x")
			countofx++;
		else if(b4=="o")
			countofo++; 
		else if(b4=="+")
			countofp++; 
		
		if(b5=="x")
			countofx++;
		else if(b5=="o")
			countofo++; 
		else if(b5=="+")
			countofp++; 
	
	
		if(b6=="x")
			countofx++;
		else if(b6=="o")
			countofo++; 
		else if(b6=="+")
			countofp++; 
	
	
		if(b7=="x")
			countofx++;
		else if(b7=="o")
			countofo++; 
		else if(b7=="+")
			countofp++; 
	
	
		if(b8=="x")
			countofx++;
		else if(b8=="o")
			countofo++; 
		else if(b8=="+")
			countofp++; 
	
	
		if(b9=="x")
			countofx++;
		else if(b9=="o")
			countofo++; 
		else if(b9=="+")
			countofp++; 

		if(b10=="x")
			countofx++;
		else if(b10=="o")
			countofo++; 
		else if(b10=="+")
			countofp++; 

		if(b11=="x")
			countofx++;
		else if(b11=="o")
			countofo++; 
		else if(b11=="+")
			countofp++; 

		if(b12=="x")
			countofx++;
		else if(b12=="o")
			countofo++; 
		else if(b12=="+")
			countofp++; 

		if(b13=="x")
			countofx++;
		else if(b13=="o")
			countofo++; 
		else if(b13=="+")
			countofp++; 

		if(b14=="x")
			countofx++;
		else if(b14=="o")
			countofo++; 
		else if(b14=="+")
			countofp++; 

		if(b15=="x")
			countofx++;
		else if(b15=="o")
			countofo++; 
		else if(b15=="+")
			countofp++; 

		if(b16=="x")
			countofx++;
		else if(b16=="o")
			countofo++; 
		else if(b16=="+")
			countofp++; 

		if(b17=="x")
			countofx++;
		else if(b17=="o")
			countofo++; 
		else if(b17=="+")
			countofp++; 

		if(b18=="x")
			countofx++;
		else if(b18=="o")
			countofo++; 
		else if(b18=="+")
			countofp++; 

		if(b19=="x")
			countofx++;
		else if(b19=="o")
			countofo++; 
		else if(b19=="+")
			countofp++; 

		if(b20=="x")
			countofx++;
		else if(b20=="o")
			countofo++; 
		else if(b20=="+")
			countofp++; 

		if(b21=="x")
			countofx++;
		else if(b21=="o")
			countofo++; 
		else if(b21=="+")
			countofp++; 

		if(b22=="x")
			countofx++;
		else if(b22=="o")
			countofo++; 
		else if(b22=="+")
			countofp++; 

		if(b23=="x")
			countofx++;
		else if(b23=="o")
			countofo++; 
		else if(b23=="+")
			countofp++; 

		if(b24=="x")
			countofx++;
		else if(b24=="o")
			countofo++; 
		else if(b24=="+")
			countofp++; 

		if(b25=="x")
			countofx++;
		else if(b25=="o")
			countofo++; 
		else if(b25=="+")
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

	var b1=document.getElementById(1).value; 
	var b2=document.getElementById(2).value ;
	var b3=document.getElementById(3).value ;
	var b4=document.getElementById(4).value ;
	var b5=document.getElementById(5).value ;
	var b6=document.getElementById(6).value ;
	var b7=document.getElementById(7).value ;
	var b8=document.getElementById(8).value ;
	var b9=document.getElementById(9).value ;
	var b10=document.getElementById(10).value ;
	var b11=document.getElementById(11).value ;
	var b12=document.getElementById(12).value ;
	var b13=document.getElementById(13).value ;
	var b14=document.getElementById(14).value ;
	var b15=document.getElementById(15).value ;
	var b16=document.getElementById(16).value ;
	var b17=document.getElementById(17).value ;
	var b18=document.getElementById(18).value ;
	var b19=document.getElementById(19).value ;
	var b20=document.getElementById(20).value ;
	var b21=document.getElementById(21).value ;
	var b22=document.getElementById(22).value ;
	var b23=document.getElementById(23).value ;
	var b24=document.getElementById(24).value ;
	var b25=document.getElementById(25).value ;


	if(b1=="o" && b2=="o" && b3=="o" && b4=="o" && b5=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b1=="x" && b2=="x" && b3=="x" && b4=="x" && b5=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b1=="+" && b2=="+" && b3=="+"&& b4=="+" && b5=="+")

					{	
						alert(" + won Please reset the game.");
					}
	
	if(b6=="o" && b7=="o" && b8=="o" && b9=="o" && b10=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b6=="x" && b7=="x" && b8=="x" && b9=="x" && b10=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b6=="+" && b7=="+" && b8=="+"&& b9=="+" && b10=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b11=="o" && b12=="o" && b13=="o" && b14=="o" && b15=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b11=="x" && b12=="x" && b13=="x" && b14=="x" && b15=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b11=="+" && b12=="+" && b13=="+"&& b14=="+" && b15=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b16=="o" && b17=="o" && b18=="o" && b19=="o" && b20=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b16=="x" && b17=="x" && b18=="x" && b19=="x" && b20=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b16=="+" && b17=="+" && b18=="+"&& b19=="+" && b20=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b21=="o" && b22=="o" && b23=="o" && b24=="o" && b25=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b21=="x" && b22=="x" && b23=="x" && b24=="x" && b25=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b21=="+" && b22=="+" && b23=="+"&& b24=="+" && b25=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b1=="o" && b6=="o" && b11=="o" && b16=="o" && b21=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b1=="x" && b6=="x" && b11=="x" && b16=="x" && b21=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b1=="+" && b6=="+" && b11=="+"&& b16=="+" && b21=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b2=="o" && b7=="o" && b12=="o" && b17=="o" && b22=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b2=="x" && b7=="x" && b12=="x" && b17=="x" && b22=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b2=="+" && b7=="+" && b12=="+"&& b17=="+" && b22=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b3=="o" && b8=="o" && b13=="o" && b18=="o" && b22=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b3=="x" && b8=="x" && b13=="x" && b18=="x" && b22=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b3=="+" && b8=="+" && b13=="+"&& b18=="+" && b22=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b4=="o" && b9=="o" && b14=="o" && b19=="o" && b24=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b4=="x" && b9=="x" && b14=="x" && b19=="x" && b24=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b4=="+" && b9=="+" && b14=="+"&& b19=="+" && b24=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b5=="o" && b10=="o" && b15=="o" && b20=="o" && b25=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b5=="x" && b10=="x" && b15=="x" && b20=="x" && b25=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b5=="+" && b10=="+" && b15=="+"&& b20=="+" && b25=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b1=="o" && b7=="o" && b13=="o" && b19=="o" && b25=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b1=="x" && b7=="x" && b13=="x" && b19=="x" && b25=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b1=="+" && b7=="+" && b13=="+"&& b19=="+" && b25=="+")

					{	
						alert(" + won Please reset the game.");
					}
		if(b5=="o" && b9=="o" && b13=="o" && b17=="o" && b21=="o")
					{	
						alert(" o won Please reset the game.");
					}
		if(b5=="x" && b9=="x" && b13=="x" && b17=="x" && b21=="x")

					{	
						alert(" x won Please reset the game.");
					}
		if(b5=="+" && b9=="+" && b13=="+"&& b17=="+" && b21=="+")

					{	
						alert(" + won Please reset the game.");
					}
		
		if(tot==24)
		{
			alert("draw Please reset the game.");
		}
}