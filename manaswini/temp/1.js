<html>
<head>
<link rel="stylesheet" type="text/css" href="wea.css">
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<script>
$(document).ready(function(){
    $("button").click(function(){
        $.ajax({url: "http://localhost:1111/", success: function(result){
            for(var i=1;i<10;i++)
            {
            $("#con").append('<div class="row"><div class="col-sm-3"><img src="'+result[i].show_key_art+'"/></div><div class="col-sm-9">+<p style="color:black;"><b>Title:</b></p><p style="color:white">'+result[i].title+"</p>"+'<p style="color:black" id="des"><b>Description:<b></p><p style="color:white">'+result[i].synopsis["short-synopsis"]+"<span data-toggle='modal' data-target='#myModal' class='seemore' data-synop='"+result[i].synopsis["full-synopsis"]+"' data-msynop='"+result[i].synopsis["medium-synopsis"]+"' class='btn-default'>see more</span>" +'<p style"color:black"><b>Audio:</b></p><p style="color:white">'+result[i].audio+'</p>'+'<p style="color:black"><b>Ratings:</b></p><p style="color:white">'+result[i].ratings+'</p></div></div>');
            for(var j=0; j<result[i].videos.length ;j++){
              
                        $("#con").append(result[i].videos[j].episode_title+ ' ----- ' + result[i].videos[j].season+ '<br>');
                          }   
            $("#con").append("<hr>");
            }
            $("#des").click(function(){
                $("#popup").append(result[i].synopsis["full-synopsis"]);
            });
            $(".seemore").click(function(){
                var synop = $(this).data("synop");
                if(synop == "undefined"){
                    synop = $(this).data("msynop");
                }
                $("#full-synop").html(synop);
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
</script>
</script>
</head>
<body>
  <div id="con" class="container"></div>
    <button>Get JSON data</button> 
    <button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>

    <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
    
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title">Modal Header</h4>
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          
        </div>
        <div class="modal-body">
          <p id="full-synop"></p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
        </div>
      </div>
      
    </div>
</div>

</body>
</html>