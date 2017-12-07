from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from foursquare import Foursquare
import json
from yelpapi import YelpAPI
from .models import CheckIn
from django.contrib.auth.decorators import login_required


yelp_api = YelpAPI(client_id='yjbKgmVwUQdd_qmGCHs0zg', client_secret='7NzN5SbUXhqq5Ktqhub7AMkaLwj1E0p7Hrp76gK00UE9bB5EkiwTg3AEVYA3DtTW')

switch = False


def api(request, place):
    data = yelp_api.search_query(location=place)
    arr = []
    for i in data['businesses']:

        json = {
            'id': i['id'],
            'name': i['name'],
            'image': i['image_url'],
            'location': i['location']['address1'],
            'city': i['location']['city'],
            'country': i['location']['country'],
            'url': i['url'],
            'phone': i['display_phone'],
        }

        arr.append(json)
    return JsonResponse(arr, safe=False)



def home(request):
    return render(request, 'places/home.html')

@login_required
def checkin(request):

    id = request.GET['id']
    c = CheckIn.objects.create(buttonId=id, status=True, owner=request.user)
    c.save()
    filter_by_user = CheckIn.objects.filter(owner=request.user)
    return render(request, 'places/home.html', {'checkin': filter_by_user})

