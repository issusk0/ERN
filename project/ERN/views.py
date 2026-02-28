import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.



#api for requesting a build
def build(request,id):
        data = {'Hola':'hola'}
        return JsonResponse(data)


#api for adding a build by the user
def add_build(request):
    if request.method == "POST":
        #expecting {relic Xn: the elements of that relic, character X: char} 
        #example {relic_1: buffs attack power, character: revenant}
        build = json.loads(request.body)
        
