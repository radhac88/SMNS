$(document).ready(function () {
    var paginationItems = function (done) {
        $.ajax({
            type: 'GET',
            url: 'http://localhost:1111',
            success: function (response) {
                done(response);
            }
        });
    }

    function handlePaginationClick(newPageIndex, paginationNavigation) {
        var paginationItems = $(paginationNavigation).data('paginationItems'),
            startItem = newPageIndex * this.items_per_page,
            endItem = Math.min(startItem + this.items_per_page, paginationItems.length),
            i,
            newContent = '';
        // This selects 20 elements from a content array
        for (i = startItem; i < endItem; i += 1) {
            newContent += '<li>' + paginationItems[i] + '</li>';
        }
        $('#paginationContent').html(newContent);
        return false;
    }

    $("#paginationNavigation")
        .data('paginationItems', paginationItems)
        .pagination(paginationItems.length, {
            items_per_page: 4,
            callback: handlePaginationClick
        });

    $.ajax({
        url: "http://localhost:1111", success: function (result) {
            $("#data-grid").css("display", "block")
            for (var i = 0; i < result.length; i++) {
                var clone = $("#data-grid").clone();
                clone.find("#showimg").attr("src", result[i].show_key_art);
                clone.find("#showtitle").html(result[i].title);
                clone.find("#des").html(result[i].synopsis["short-synopsis"]);
                clone.find("#showlang").html(result[i].audio);
                clone.find("#showrating").html(result[i].ratings);
                clone.find(".seemore").data('synop', result[i].synopsis["long-synopsis"]);
                clone.find(".seemore").data('msynop', result[i].synopsis["medium-synopsis"]);
                $("#image-container").append(clone);
                // for (var j = 0; j < result[i].videos.length; j++) {
                //     $("#image-container").append('<div id=video-container class="col-sm-6"><img src="' + result[i].videos[j].video_thumbnail + '"/></div>'
                //         + 'episode:' + result[i].videos[j].episode_title + '<br>'
                //         + 'Ratings:' + result[i].videos[j].ratings + '<br>'
                //         + 'season:' + result[i].videos[j].season + '<br>');
                // }
            }
            $(".seemore").click(function () {
                var synop = $(this).data("synop");
                if (synop == "undefined") {
                    synop = $(this).data("msynop");
                }
                $("#full-synop").html(synop);
            });
        }
    });

});//ready func close

//scroll function
window.onscroll = function () { scrollFunction() };
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
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