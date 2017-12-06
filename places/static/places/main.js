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
       // var json = JSON.parse(data)
        data.forEach(function(obj) {
            var block = createBlock(obj)
            places.appendChild(block)
        })

    }


    //create the div with needed info
    function createBlock(obj) {
        var div = document.createElement('div');
        var img = document.createElement('img');
        var h5 = document.createElement('h5');
        var address = document.createElement('address');

        // div.setAttribute('style', 'width: 30%');
        img.setAttribute('src', obj.image);
        img.setAttribute('style', 'width: 80px; height: 80px')
        address.innerHTML ="Address: " + obj.city
            + obj.location + "<br/>"
            + "Phone: " + obj.phone;
        h5.innerHTML = obj.name;
        div.appendChild(h5);
        div.appendChild(img);
        div.appendChild(address)

        return div;
    }


    });