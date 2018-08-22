$(document).ready(function(){
	var movies = [];
	$.ajax({
        type: 'GET',
        url: 'http://localhost:1111',
        success: function (response) {
            movies = response;
        }
         $("#page-content").append('<div class="row"><div class="col-sm-3"><img src="'
                            + movies[i].show_key_art + '" class="img-rounded" class="img-responsive"  onerror="imgError(this);" /></div><div class="col-sm-9"><b><i>Title: </i></b>'
                            + movies[i].title + '<p id="des"><b><i>Description: </i></b>"'
                            + movies[i].synopsis["short-synopsis"]
                            + "...<span data-toggle ='modal' data-target= '#myModal'class='seemore' data-synop='"
                            + movies[i].synopsis["full-synopsis"] + "'data-mysynop = '"
                            + movies[i].synopsis["medium-synopsis"] + "' class='btn-default'>seemore</span>"
                            + '"<p><b><i>language: </i></b></p>"'
                            + movies[i].audio + ' "<p><b><i>Ratings: </i></b>"'
                            + movies[i].ratings
                            + '<span id="ldc'+i+'"></span>'
                            + '"</p><button class="loadmore">load more</button></div></div>'
                        );
         $("#list").append('<li data-target="#myCarousel" data-slide-to="0" class="active"></li>');
  		 $("#ep").append( '<div class="item active"><img src="'+ movies[id1].videos[0].video_image+'"></div>');

  		 for (var j=1;j<movies[].videos.length;j++) {
  		 	 $("#list").append('<li data-target="#myCarousel" data-slide-to="'+j+'"></li>');
        $("#ep").append( '<div class="item"><img src="'+ result[id1].videos[j].video_image+'"></div>');
                }
      	});