function myFuntion(m) {
	// body...
	var noofx=0;
	var noofo=0;
	var i;
	for(i=1; i<=9; i++)
	{
		if (document.getElementById(i).value==x)
		noofx++;  
			else if (document.getElementById(i).value==o)
				noofo++;
	}
	b=m;
	
	if(noofx==noofo)
		document.getElementById(b).value="x";
	else
		document.getElementById(b).value="o"

	}
	
	
	
	if (document.getElementById("1").value=="x")
			noofx++;  
		else if (document.getElementById("1").value=="o")
			noofo++;
	
	else
		document.getElementById(b).value="o";
