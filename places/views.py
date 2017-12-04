from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from foursquare import Foursquare
import json


client = Foursquare(client_id='ZOHSQDAX213QVTFLWXMDQNGQWCZOZIX3SLZKDEZI00H30AHD', 
                    client_secret='5PBAEWTG1IHDQ52I3ETE14JGV3N2PAYOY0VPTB2U4NNIF2B0')



def homepage(request):
    
    venue_search = client.venues.explore(params={
        'near': 'Tirana'
    })

    
    arr = []
    for i in venue_search['groups'][0]['items']:
        
        json = {
            'id': i['venue']['id'],
            'name': i['venue']['name'],
        }
        arr.append(json)
    return JsonResponse(arr, safe=False)