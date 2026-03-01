import json
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from . import models
from . import utils

#api for requesting a build
class Request_Build(View):
    def get(self,request,id):
            data = {'Hola':'hola'}
            return JsonResponse(data)



class Add_Build(View):
#api for adding a build by the user
    def set(self,request):
        if request.method == "POST":
            #expecting {relic Xn: the elements of that relic, character X: char} 
            #example {relic_1: buffs attack power, character: revenant}
            build = json.loads(request.body)
        



class Add_Normal_Relic(View):
    def post(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            icon = utils.Helpers.get_relic_icon_cached(data.get('relic_type'))
            relic = models.Normal_Relic(name = data.get('name'),
                                        buff_1 = data.get('buff_1'),
                                        buff_2 = data.get('buff_2'),
                                        buff_3 = data.get('buff_3'),
                                        icon_relic = icon,
                                        relic_type = data.get('relic_type'),
                                        relic_color = data.get('relic_color'))
            relic.save()
           
        
                
    
          
