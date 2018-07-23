function x(m) {
	
		var countofo=0;
		var countofx=0;
		var b=[];
		for(var i=1;i<10;i++)
		{
			b[i] = document.getElementById(i).value; 
		}
		for(var i=1;i<10;i++)
		{
			if(b[i]=="x")
			countofx++;
			else if(b[i]=="o")
			countofo++; 
		}

		
		
var	p=m;
var tot=countofo+countofx;



	
	if(countofx==countofo)
	{
		document.getElementById(p).value = "x";

		
		var ran=Math.floor((Math.random()*9) + 1); 
	
			while(document.getElementById(ran).value=="o"||document.getElementById(ran).value=="x")
			{
				ran=Math.floor((Math.random()*9) + 1);
			}
		setTimeout(function(){document.getElementById(ran).value ="o"; }, 1000);
		win();
						if(tot==8)
							{
							document.getElementById("demo").innerHTML= "Draw Please reset the game.";
							}

	}
}
function re()
{
	for(var i=1;i<10;i++)
		{
		 document.getElementById(i).value = ""; 
		}
	document.getElementById("demo").innerHTML="players turn";
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

		if(b1=="o" && b2=="o" && b3=="o")
					{	
						col(1,2,3);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b1=="x" && b2=="x" && b3=="x")
					{	
						col(1,2,3);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(b4=="o" && b5=="o" && b6=="o")
					{
						col(4,5,6);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b4=="x" && b5=="x" && b6=="x")
					{
						col(4,5,6);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(b7=="o" && b8=="o" && b9=="o")
					{
						col(7,8,9);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b7=="x" && b8=="x" && b9=="x")
					{
						col(7,8,9);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(b1=="o" && b4=="o" && b7=="o")
					{
						col(1,4,7);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b1=="x" && b4=="x" && b7=="x")
					{
						col(1,4,7);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(b2=="o" && b5=="o" && b8=="o")
					{
						col(2,5,8);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b2=="x" && b5=="x" && b8=="x")
					{
						col(2,5,8);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(b3=="o" && b6=="o" && b9=="o")
					{
						col(3,6,9);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b3=="x" && b6=="x" && b9=="x")
					{
						col(3,6,9);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(b1=="o" && b5=="o" && b9=="o")
					{
						col(1,5,9);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b1=="x" && b5=="x" && b9=="x")
					{
						col(1,5,9);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(b3=="o" && b5=="o" && b7=="o")
					{
						col(3,5,7);
						document.getElementById("demo").innerHTML= "o won Please reset the game.";
					}
		if(b3=="x" && b5=="x" && b7=="x")
					{
						col(3,5,7);
						document.getElementById("demo").innerHTML= "x won Please reset the game.";
					}
		if(tot==8)
				{
				alert("draw Please reset the game.");
				}
		

}