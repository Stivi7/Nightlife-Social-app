from django.shortcuts import render, redirect
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
    all = CheckIn.objects.all()
    return render(request, 'places/home.html', {'check': all})

@login_required(login_url='https://api.twitter.com/oauth/authenticate?oauth_token=RGP-'
                          '1AAAAAAA3ht3AAABYDgXdLU&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2'
                          'Foauth%2Fcomplete%2Ftwitter%2F%3Fredirect_state%3D5Rl65p7gK93rfcseIjnfFR6hXwkjOYho')
def checkin(request):

    id = request.GET['id']
    c, created = CheckIn.objects.get_or_create(buttonId=id, owner=request.user)
    c.save()


    if (c.status == True and c.owner == request.user):
        c.status = False
        c.save()

    elif (c.status == False and c.owner == request.user):
        c.status = True
        c.save()


    return redirect('home')

