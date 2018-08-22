$(document).ready(function () {
    var movies = [];
    function show() {
        $('#loading').hide();
        $('#container').fadeIn(2000);
    };
    $.ajax({
        type: 'GET',
        url: 'http://localhost:1111',
        success: function (response) {
            movies = response;
        },
        complete: function () {
            $('#pagination').twbsPagination({
                totalPages: movies.length / 10,
                visiblePages: 10,
                onPageClick: function (event, page) {
                    $("#page-content").html("");
                    let startIndex = (page - 1) * 10;
                    let endIndex = (page * 10) - 1;
                    // console.log(""+page);
                    for (var i = startIndex; i < endIndex; i++) {
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
                            + '<div><span id="ldc'+i+'" class="menu"></span>'
                            + '"</p><button class="loadmore" >load more</button></div><br><button class="btn btn-success"><a href="carousel.html?id='+i+'">show</a></button></div></div>'
                        );

                        for (var j = 0; j < movies[i].videos.length; j++) {
                            $("#ldc" + i).append('<div><div class="row"><div class="col-sm-3"><p><b>thumbnail</b></p><img src="' 
                                + movies[i].videos[j].video_thumbnail 
                                + '" class="img-responsive" width="150px" height="130px";/></div><div class="col-sm-9"><br><p><b>episode title</p></b><p>' 
                                + movies[i].videos[j].episode_title 
                                + '</p><p><b>season</b></p><p>' 
                                + movies[i].videos[j].season + '</p><p><b>ratings</p></b><p>' 
                                + movies[i].videos[j].ratings + '</p></div></div></div>');

                        }
                        $("#page-content").append("<div><hr></div>");
                    }

                    
                    $('.loadmore').click(function () {
                        $('.menu').toggle();
                    });
                    

                    $(".seemore").click(function () {
                        var synop = $(this).data("synop");
                        if (synop == "undefined") {
                            synop = $(this).data("mysynop");
                        }
                        var rep = synop.replace(/[\u21b5\u21e5]/g, " ")
                        $("#full-synop").html(rep);
                    });
                    $("#topBtn").click();
                }
            }).on('page', function (event, page) {
                // console.info(page + ' (from event listening)');
            });
            show();
        }//ajax complete function end
    });
});//ready func close

//scroll function
window.onscroll = function () { scrollFunction() };
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("topBtn").style.display = "block";
    } else {
        document.getElementById("topBtn").style.display = "none";
    }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
// for dummy image
function imgError(image) {
    image.onerror = "";
    image.src = "./images/inf.jpg";
    return true;
}