import json
import pdb
from django.http import JsonResponse



def api_home(request):
    body = request.body
     
    data={}
    
    try:
        data = json.loads(body)
    except:
        pass
    data['headers'] = dict(request.headers)
    return JsonResponse(data)