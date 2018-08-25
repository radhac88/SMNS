$(document).ready(function(){
    $("button").click(function(){
        $.ajax({url: "http://localhost:1111/", success: function(result){
        	for(var i=10;i<20;i++)
        	{
            $("#con").append('<div class="section"><div class="col-sm-6"><div class="col-sm-3"></div><img class="img-responsive" src="'+result[i].show_key_art+'"/></div><div class="col-sm-9">'+'<p style="color:black;"><b>Title:</b></p><p style="color:white">'+result[i].title+"</p>"+'<p style="color:black" id="des"><b>Description:<b></p><p style="color:white">'+result[i].synopsis["short-synopsis"]+"<span data-toggle='modal' data-target='#myModal' class='seemore' data-synop='"+result[i].synopsis["full-synopsis"]+"' data-msynop='"+result[i].synopsis["medium-synopsis"]+"' class='btn-default'>see more</span>" +'<p style"color:black"><b>Audio:</b></p><p style="color:white">'+result[i].audio+'</p>'+'<p style="color:black"><b>Ratings:</b></p><p style="color:white">'+result[i].ratings+'</p></div></div>');
            
                    function func(){ 
                        for(var j=0; j<result[i].videos.length ;j++){
                            $("#con").append('<p><b>episode title</p></b><p>'+result[i].videos[j].episode_title+'</p>'
                                +'<p><b>season</p></b><p>'+result[i].videos[j].season+'</p>'
                                +'<p><b>ratings</p></b><p>'+result[i].videos[j].ratings+'</p><br>');
                        }
                    }
     
            }
            $("#des").click(function(){
                $("#popup").append(result[i].synopsis["full-synopsis"]);
            });
            $(".seemore").click(function(){
                var synop = $(this).data("synop");
                if(synop == "undefined"){
                    synop = $(this).data("msynop");
                  }
                var txt=synop.replace(/[\u21e5\u21b5]/g," ")
                $("#full-synop").html(txt);
            });
        
        }});
    });
 
});  



           
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
   }
}


function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;

}

