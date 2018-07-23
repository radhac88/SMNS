function x(m) {
	

var	p=m;
 for(i=0;i<9;i++)
 {
	if(i==0||i==2||i==4||i==6||i==8)
	{
		document.getElementById(p).value = "x";
	}
	else
	{
		document.getElementById(p).value = "o";
	}
  return i;  			
}			
}
