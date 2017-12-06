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
        places.innerHTML = "";

        data.forEach(function(obj) {
            var block = createBlock(obj)
            places.appendChild(block)
        })

    }

    // create imasge element
    function createImage(obj) {
        var img = document.createElement('img');
        img.setAttribute('src', obj.image);
        img.setAttribute('style', 'width: 80px; height: 80px');

        return img;
    }

    // create h5 for place's name
    function createH(obj) {
        var h5 = document.createElement('h5');
        h5.innerHTML = obj.name;
        return h5;
    }

    //location address
    function createAddress(obj) {
        var address = document.createElement('address');
        address.innerHTML ="Address: " + obj.city
            + obj.location + "<br/>"
            + "Phone: " + obj.phone;
        return address;
    }

    //create button for 'going' 'not going'
    function createButton(obj) {
        var btn = document.createElement('button')
        btn.setAttribute('class', 'btn btn-default btn-outline-primary');
        btn.setAttribute('id', obj.id);
        btn.innerHTML = '0';
        return btn;
    }

    //create the div with needed info
    function createBlock(obj) {
        var div = document.createElement('div');
        var span = document.createElement('span');
        var divrow = document.createElement('div');
        var img = createImage(obj);
        var h5 = createH(obj);
        var address = createAddress(obj);
        var button = createButton(obj);
        span.innerHTML = 'Going';
        div.setAttribute('class', 'data-div');
        // divrow.setAttribute('class', 'row');
        divrow.appendChild(h5);
        divrow.appendChild(span);
        divrow.appendChild(button);

        div.appendChild(divrow);
        div.appendChild(img);
        div.appendChild(address);

        return div;
    }


    });