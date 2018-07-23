	if(((document.getElementById("1").value=="x")||(document.getElementById("1").value=="o"))&&(document.getElementById("1").value==document.getElementById("2").value)&&(document.getElementById("3").value))
		{
			document.getElementById("demo").innerHTML="player "+document.getElementById("1").value+"wins";
		}
	else if (((document.getElementById("4").value=="x")||(document.getElementById("4").value=="o"))&&(document.getElementById("4").value==document.getElementById("5").value)&&(document.getElementById("5").value==document.getElementById("6").value))
			{
			document.getElementById("demo").innerHTML="player "+document.getElementById("4").value+"wins";
		}
	else if(((document.getElementById("7").value=="x")||(document.getElementById("7").value=="o"))&&(document.getElementById("7").value==document.getElementById("8").value)&&(document.getElementById("8").value==document.getElementById("9").value))
			{
			document.getElementById("demo").innerHTML="player "+document.getElementById("7").value+"wins";
		}
	else if(((document.getElementById("1").value=="x")||(document.getElementById("1").value=="o"))&&(document.getElementById("1").value==document.getElementById("4").value)&&(document.getElementById("4").value==document.getElementById("7").value))
		{
			document.getElementById("demo").innerHTML="player "+document.getElementById("1").value+"wins";
		}
	else if(((document.getElementById("2").value=="x")||(document.getElementById("2").value=="o"))&&(document.getElementById("2").value==document.getElementById("5").value)&&(document.getElementById("5").value==document.getElementById("8").value))
		{
			document.getElementById("demo").innerHTML="player "+document.getElementById("2").value+"wins";
		}
	else if(((document.getElementById("3").value=="x")||(document.getElementById("3").value=="o"))&&(document.getElementById("3").value==document.getElementById("6").value)&&(document.getElementById("2").value==document.getElementById("9").value))
		{
			document.getElementById("demo").innerHTML="player "+document.getElementById("3").value+"wins";
		}
	else if(((document.getElementById("1").value=="x")||(document.getElementById("1").value=="o"))&&(document.getElementById("1").value==document.getElementById("5").value)&&(document.getElementById("5").value==document.getElementById("9").value))
		{
			document.getElementById("demo").innerHTML="player "+document.getElementById("1").value+"wins";
		
	else if(((document.getElementById("3").value=="x")||(document.getElementById("3").value=="o"))&&(document.getElementById("3").value==document.getElementById("5").value)&&(document.getElementById("5").value==document.getElementById("7").value))
		{
			document.getElementById("demo").innerHTML="player "+document.getElementById("3").value+"wins";
		}
	






















	
function winDetect()
{
	var a=document.getElementById("1").value;
		var b=document.getElementById("2").value;
        var c=document.getElementById("3").value;
        var d=document.getElementById("4").value;
        var e=document.getElementById("5").value;
        var f=document.getElementById("6").value;
        var g=document.getElementById("7").value;
        var h=document.getElementById("8").value;
		var i=document.getElementById("9").value;
		if (var a== var b && var c)
		{
			window.alert("Game won. Please reset the game.");
			return a;
		}
		else if (var d== var e && var f)
		{
			window.alert("Game won. Please reset the game.");
			return d;
		}
		else if (var g== var h && var i)
		{
			window.alert("Game won. Please reset the game.");
			return g;
		}
		else if (var a== var e && var i)
		{
			window.alert("Game won. Please reset the game.");
			return a;
		}
		else if (var c== var e && var g)
		{
			window.alert("Game won. Please reset the game.");
			return c;
		}
		else if (var a== var d && var g)
		{
			window.alert("Game won. Please reset the game.");
			return a;
		}
		else if (var b== var e && var h)
		{
			window.alert("Game won. Please reset the game.");
			return b;
		}
		else if (var c== var f && var i)
		{
			window.alert("Game won. Please reset the game.");
			return c;
		}


}