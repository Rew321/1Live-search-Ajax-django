from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from searchapp.models import Webseries
from django.http import JsonResponse


# Create your views here.



def home(request):
    return render(request, 'index.html')




def search_result(request):
    if request.is_ajax():
        res = None
        series = request.POST.get('series')
        query_se = Webseries.objects.filter(name__icontains=series)
        
        if len(query_se) > 0 and len(series) > 0:
            data = []
            for pos in query_se:
                item = {
                    'pk':pos.pk,
                    'name':pos.name,
                    'image':pos.image,
                }

                data.append(item)
            res = data
        else:
            res = 'No Webseries found with that name'
        
        return JsonResponse({'data':res})
    return JsonResponse({})      

def detail_series(request, pk):
    series_obj = Webseries.objects.get(pk=pk)
    
    return render(request, 'detail.html', context={'series':series_obj})      
