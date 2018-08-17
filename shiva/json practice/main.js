$(document).ready(function () {
    $("#b1").click(function () {
        $.ajax({
            url: "http://localhost:1111/", success: function (result) {
                for (var i = 0; i < result.length; i++) {
                    $("#image-container").append('<div class="row"><div class="col-sm-3"><img src="'
                        + result[i].show_key_art + '"/></div><div class="col-sm-9"><b>Title:</b>"'
                        + result[i].title + ' "<p id="des"><b>Description:</b>"'
                        + result[i].synopsis["short-synopsis"]
                        + "...<span data-toggle ='modal' data-target= '#myModal'class='seemore' data-synop='" + result[i].synopsis["full-synopsis"] + "'data-mysynop = '" + result[i].synopsis["medium-synopsis"] + "' class='btn-default'>seemore</span>"
                        + '"<p><b>language:</b></p>"'
                        + result[i].audio + ' "<p><b>Ratings:</b>"'
                        + result[i].ratings
                        + "</p> </div></div>");
                    /*for(var j=0; j<result[i].videos.length ;j++){
                        $("#image-container").append(result[i].videos[j].episode_title+ '----' +result[i].videos[j].season +'<br>');
                    }*/
                    $("#image-container").append("<div><hr></div>");
                }
                $(".seemore").click(function () {
                    var synop = $(this).data("synop");
                    if (synop == "undefined") {
                        synop = $(this).data("mysynop");
                    }
                    var rep = synop.replace(/[\u21b5\u21e5]/g, " ")
                    $("#full-synop").html(rep);
                });
            }
        });
    });

});
window.onscroll = function () { scrollFunction() };
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById('myBtn').style.display = "block";
    }
    else {
        document.getElementById('myBtn').style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}