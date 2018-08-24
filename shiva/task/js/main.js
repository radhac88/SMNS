$(document).ready(function () {
    var movies = [];
    $('#error').hide();
    function show() {
        $('#loading').hide();
        $('#error').hide();
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
                            + movies[i].show_key_art + '"  class="img-responsive img-rounded"  onerror="imgError(this);" /></div><div class="col-sm-9"><b><i>Title: </i></b>'
                            + movies[i].title + '<p id="des"><b><i>Description: </i></b>'
                            + movies[i].synopsis["short-synopsis"]
                            + "...<span data-toggle ='modal' data-target= '#myModal'class='seemore' data-synop='"
                            + movies[i].synopsis["full-synopsis"] + "'data-mysynop = '"
                            + movies[i].synopsis["medium-synopsis"] + "' class='btn-default'>seemore</span>"
                            + '<p><b><i>language: </i></b></p>'
                            + movies[i].audio + '<p><b><i>Ratings: </i></b>'
                            + movies[i].ratings
                            + '<br /> <br /> <button class="btn btn-info" id="showInfoBtn' + i + '" onclick="showInfo(' + i + ')">Show Seasons</button>  <button class="btn btn-success"><a href="carousel.html?id=' + i + '" target="_blank" title="This will open in another tab">Additional Information</a></button></div></div>'
                            + '<div><span id="menu' + i + '"style="display:none"></span>'
                        );

                        for (var j = 0; j < movies[i].videos.length; j++) {
                            $("#menu" + i).append('<div><div class="row"><div class="col-sm-3"></div><div class="col-sm-3"><p><b>Thumbnail</b></p><img class="img-thumbnail img-responsive"  src="'
                                + movies[i].videos[j].video_thumbnail
                                + '" width="150px" height="130px"/></div><div class="col-sm-6"><br><p><b>Episode Title</p></b><p>'
                                + movies[i].videos[j].episode_title
                                + '</p><p><b>Season</b></p><p>'
                                + movies[i].videos[j].season + '</p><p><b>atings</p></b><p>'
                                + movies[i].videos[j].ratings + '</p></div></div></div>');

                        }
                        $("#page-content").append("<div><hr></div>");
                    }
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
//for show information (toggle)
function showInfo(id) {
    $('#menu' + id).toggle();
    if ($('#menu' + id).css('display') == 'none') {
        $("#showInfoBtn" + id).html('Show Seasons')
    } else {
        $("#showInfoBtn" + id).html('Hide Seasons')
    }
};

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
    image.src = "./images/inf.svg";
    return true;
}