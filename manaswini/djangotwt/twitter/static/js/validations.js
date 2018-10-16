
$(document).ready(function(){
	$("#save").unbind('submit').submit(function(){
	// function phonenumber(inputtext,alert){
		var phone = $("id_phonenumber").val();
		var phone = phone.replace(/[^0-9]/g, '');
		if(phone.length != 10) { 
   		alert("not 10 digits");
		} 
		else if(tel.startsWith("9") || tel.startsWith("8") || tel.startsWith("7")){
		return true;
		}
	}
	function emailValidation(){
		var emailExp = $("id_email").val();
		var emailExp = /^[w-.+]+@[a-zA-Z0-9.-]+.[a-zA-z0-9]{2,4}$/;
		if(inputtext.value.match(emailExp)){
		return true;
		}else{
		alert("please enter valid email id");
		inputtext.focus();
		return false;
		}
	}
	function password(){
		var psw = $("#id_password").val();
		if (psw.length < 4) {
  			alert("Your password needs a minimum of four characters")
		} else if (psw.search(/[a-z]/) < 0) {
  			alert("Your password needs a lower case letter")
		} else if(psw.search(/[A-Z]/) < 0) {
  			alert("Your password needs an uppser case letter")
		} else  if (psw.search(/[0-9]/) < 0) {
  			alert("Your password needs a number")
		} else {
			return true;
  		
		}
	}









	});
});