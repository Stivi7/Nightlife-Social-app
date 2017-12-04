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
    itemTips = []
    itemVenue = {}
    data = venue_search['groups'][0]['items']
    
    
    for item in data:
        itemVenue = item['venue']
        itemTips = item['tips']
        
        itemTip = {}
        for tip in itemTips:
            itemTip = tip
            
            json = {
                'id': itemVenue['id'],
                'name': itemVenue['name'],
                'text': itemTip['text']
            }

            arr.append(json)
            
        print(arr)    
    return JsonResponse(arr, safe=False)  
        
         
    
    