	$(document).ready(function(){
    $("#b1").click(function(){
        $.ajax({url: "http://localhost:1111/", success: function(result){
        	for(var i=0; i<result.length ;i++){

         		$("#image-container").append('<div class="row"><div class="col-sm-3"><img src="'
         			+result[i].show_key_art +'"/></div><div class="col-sm-9"><b>Title:</b>"' 
         			+result[i].title+' "<p id="des"><b>Description:</b>"' 
         			+result[i].synopsis["short-synopsis"] +'"</p><p><b>language:</b></p>"' 
         			+result[i].audio +' "<p><b>Ratings:</b>"' 
         			+result[i].ratings 
         			+"</p> </div></div>");
         			$("#image-container").addClass("border");
         		
         		$("#image-container").append("<div><hr></div>");  
                $("#des").click(function(){
                $("#image-container").append("<div></div")
                $("iframe").toggle(1000 ,function(){
                    $("#dailog ,#image-container").append(result[i].synopsis["full-synopsis"])
                })
            })

         	
         	}
            
        }});
    });

});
