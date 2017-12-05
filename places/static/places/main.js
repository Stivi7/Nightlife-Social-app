$(document).ready(function() {

var searchButton = $("#searchBtn")
var bar = document.getElementById("searchBar")
var places = document.getElementById("places")


    searchButton.click(search)

    function search() {
        var country = bar.value
        $.ajax({
            url: '/api/' + country,
            type: 'GET',
            dataType: 'json',
            success: build,



        });
    }


    function build(data) {
       var json = JSON.parse(data)
        json.forEach(function(obj) {
            var block = createBlock(obj)
            places.appendChild(block)
        })

    }


    //create the div with needed info
    function createBlock(obj) {
        var div = document.createElement('div');
        var img = document.createElement('img');
        var h5 = document.createElement('h5');
        img.setAttribute('src', obj.image);
        h5.setAttribute(obj.name);
        div.appendChild(img);
        div.appendChild(h5);
        console.log(obj)
    }


    });