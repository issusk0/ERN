import json
from django.http import *
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from . import models
from . import utils
from django.contrib.auth.mixins import LoginRequiredMixin
#api for requesting a build
class Request_Build(View):
    def get(self,request,id):
            data = {'Hola':'hola'}
            return JsonResponse(data)


class Add_Build(LoginRequiredMixin, View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            #character searching for adding it at the build
            character = models.Character.objects.get(id=data.get('character_id'))

            relic_1 = data.get('relic_1')
            relic_2 = data.get('relic_2')
            relic_3 = data.get('relic_3')
            cursed_relic_1 = data.get('cursed_relic_1')
            cursed_relic_2 = data.get('cursed_relic_2')
            cursed_relic_3 = data.get('cursed_relic_3')

            build = models.Build(
                title=data.get('title'),
                description=data.get('description'),
                relic_1=relic_1,
                relic_2=relic_2,
                relic_3=relic_3,
                cursed_relic_1=cursed_relic_1,
                cursed_relic_2=cursed_relic_2,
                cursed_relic_3=cursed_relic_3,
                character=character,
                user=request.user,
                is_public=data.get('is_public')
            )
            build.save()
            return JsonResponse({'message': 'Build created'}, status=201)

        except models.Character.DoesNotExist:
            return JsonResponse({'message': 'Character not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
            
        

class Add_Normal_Relic(View):
    def post(self,request):
            try:
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
                return HttpResponse(status = 201)
            except json.JSONDecodeError:
                 return JsonResponse({'message': 'Invalid JSON'}, status=400)
          
#API for adding cursed relics
class Add_Cursed_Relic(View):
     


#API for users
class ERN_Users(View):