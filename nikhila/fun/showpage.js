function show(i)
{
$(document).ready(function(){

    $.ajax({url: "http://localhost:1111/", success: function(result){
    {
  
       $("#container1").append(result[i].synopsis["full-synopsis"]);   
  
    
              
        
    
      }
}});

});
}
