function x(z){
var co=0;
        var cx=0;
        if(document.getElementById(1).value=="x")
        	cx++;
        else if(document.getElementById(1).value=="o")
        	co++;
        if(document.getElementById(2).value=="x")
        	cx++;
        else if(document.getElementById(2).value=="o")
        	co++;
        if(document.getElementById(3).value=="x")
        	cx++;
        else if(document.getElementById(3).value=="o")
        	co++;
        if(document.getElementById(4).value=="x")
        	cx++;
        else if(document.getElementById(4).value=="o")
        	co++;
        if(document.getElementById(5).value=="x")
        	cx++;
        else if(document.getElementById(5).value=="o")
        	co++;
        if(document.getElementById(6).value=="x")
        	cx++;
        else if(document.getElementById(6).value=="o")
        	co++;
        if(document.getElementById(7).value=="x")
        	cx++;
        else if(document.getElementById(7).value=="o")
        	co++;
        if(document.getElementById(8).value=="x")
        	cx++;
        else if(document.getElementById(8).value=="o")
        	co++;
        if(document.getElementById(9).value=="x")
        	cx++;
        else if(document.getElementById(9).value=="o")
        	co++;
        var t=z;
       if(cx==co)
       {
        	document.getElementById(t).value="x";
        win();
    }
        else
        {
        	document.getElementById(t).value="o";
        	win();
        }
        
}
    
    function win() {
        if (document.getElementById("1").value == "x" && document.getElementById('2').value == "x" && document.getElementById('3').value=="x") 
        	alert("x won");
        else if (document.getElementById("1").value == "o" && document.getElementById('2').value == "o" && document.getElementById('3').value=="o")
        	alert("o won");
        if (document.getElementById("4").value == "x" && document.getElementById('5').value == "x" && document.getElementById('6').value=="x") 
        	alert("x won");
        else if (document.getElementById("4").value == "o" && document.getElementById('5').value == "o" && document.getElementById('6').value=="o")
        	alert("o won");
        if (document.getElementById('7').value == "x" && document.getElementById('8').value == "x" && document.getElementById('9').value=="x") 
        	alert("x won");
        else if (document.getElementById('7').value == "o" && document.getElementById('8').value == "o" && document.getElementById('9').value=="o")
        	alert("o won");


         if (document.getElementById('1').value == "x" && document.getElementById('4').value == "x" && document.getElementById('7').value=="x") 
        	alert("x won");
        else if (document.getElementById('1').value == "o" && document.getElementById('4').value == "o" && document.getElementById('7').value=="o")
        	alert("o won");
         if (document.getElementById('2').value == "x" && document.getElementById('5').value == "x" && document.getElementById('8').value=="x") 
        	alert("x won");
        else if (document.getElementById('2').value == "o" && document.getElementById('5').value == "o" && document.getElementById('8').value=="o")
        	alert("o won");
         if (document.getElementById('3').value == "x" && document.getElementById('6').value == "x" && document.getElementById('9').value=="x") 
        	alert("x won");
        else if (document.getElementById('3').value == "o" && document.getElementById('6').value == "o" && document.getElementById('9').value=="o")
        	alert("o won");

         if (document.getElementById('1').value == "x" && document.getElementById('5').value == "x" && document.getElementById('9').value=="x") 
        	alert("x won");
        else if (document.getElementById('1').value == "o" && document.getElementById('5').value == "o" && document.getElementById('9').value=="o")
        	alert("o won");

        if (document.getElementById('1').value == "x" && document.getElementById('5').value == "x" && document.getElementById('9').value=="x") 
        	alert("x won");
        else if (document.getElementById('1').value == "o" && document.getElementById('5').value == "o" && document.getElementById('9').value=="o")
        	alert("o won");

        if (document.getElementById('3').value == "x" && document.getElementById('5').value == "x" && document.getElementById('7').value=="x") 
        	alert("x won");
        else if (document.getElementById('3').value == "o" && document.getElementById('5').value == "o" && document.getElementById('7').value=="o")
        	alert("o won");

        


}
  function clearBtn() {
        status = "X"
        document.document.getElementById("1").value = "   ";
        document.document.getElementById("2").value = "   ";
        document.document.getElementById("3").value = "   ";
        document.document.getElementById("4").value = "   ";
        document.document.getElementById("5").value = "   ";
        document.document.getElementById("6").value = "   ";
        document.document.getElementById("7").value = "   ";
        document.document.getElementById("8").value = "   ";
        document.document.getElementById("9").value = "   ";
    }