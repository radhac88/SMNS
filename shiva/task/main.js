$(document).ready(function(){
    $.ajax({url: "http://localhost:1111", success: function(result){
        $("#data-grid").css("display","block")
        	for(var i=0; i<result.length ;i++){
                var clone = $("#data-grid").clone();
                clone.find("#showimg").attr("src",result[i].show_key_art);
                clone.find("#showtitle").html(result[i].title);
                clone.find("#des").html(result[i].synopsis["short-synopsis"]);
                clone.find("#showlang").html(result[i].audio);
                clone.find("#showrating").html(result[i].ratings);
                clone.find(".seemore").data('synop', result[i].synopsis["long-synopsis"]);
                clone.find(".seemore").data('msynop', result[i].synopsis["medium-synopsis"]);
                 $("#image-container").append(clone);
                for(var j=0; j<result[i].videos.length ;j++){
                    $("#image-container").append('<div id=video-container class="col-sm-6"><img src="'+result[i].videos[j].video_thumbnail+'"/></div>'
                        +'episode:'+result[i].videos[j].episode_title+'<br>'
                        +'Ratings:'+result[i].videos[j].ratings+'<br>' 
                        +'season:'+result[i].videos[j].season +'<br>');
    }
           /* for(var j=0; j<result[i].videos.length ;j++){
                $(".btn").click(function(){
            $(".container1").append('<div class="row">'
            +'<p>epsiode title:</p>'+result[i].videos[j].episode_title
            +result[i].videos[j].video_thumbnail
            +'<p>season</p>'+result[i].videos[j].season 
            +'<p>ratings</p>'+result[i].videos[j].ratings+'</div>');
               
                });
             }*/       
           
       
         	}
            $(".seemore").click(function(){
                var synop = $(this).data("synop");
                if(synop == "undefined"){
                    synop = $(this).data("msynop");
                }
                $("#full-synop").html(synop);
            });

        
    }});
});
 /*for(var j=0; j<result[i].videos.length ;j++){
        $("#image-container").append(result[i].videos[j].episode_title+ '----' +result[i].videos[j].season +'<br>');
    }
    for(var j=0; j<result[i].videos.length ;j++){
        var vclone = $("#videos-grid").clone();
        vclone.find("#.loadmore").toggle(1000).data('title',result[i].videos[j].episode_title);
        vclone.find("#ratings").data(result[i].videos[j].ratings);
        vclone.find("#season").data(result[i].videos[j].season);  
        $("#image-container").append(vclone);
    }
    */


     
//scroll function
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20){
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}