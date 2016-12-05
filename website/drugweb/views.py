from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from operator import attrgetter
# Create your views here.

from .models import Cure, Drugdetails

history_set = set()
m = 0

def index(request):
    template = loader.get_template('drugweb/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
def result(request):
    if("remove_history" in request.POST and request.POST['remove_history'] == 'yes'):
        history_set.clear()
    post_cur_drug = request.POST['cur_drug']
    post_illness_name = request.POST['illness_name']

    #temp algorithm

    query_list = list(Cure.objects.filter(illness_name__contains=post_illness_name))
    history_set.add(post_cur_drug)

    drug_result = ""
    # query_list = sorted(query_list,key = attrgetter("popularity"), reverse= True)

    # C = 7, a threshold
    # n = popularity of current drug
    # x = popularity * rating
    # m =  popularity * rating / popularity of all
    global m
    print m
    if(m == 0):
        m = weightedAverage()
    temp_list = []
    for i in query_list:
        if i.drug_name not in history_set and not(request.POST['pregnancy'] == "yes" and i.pregnancy == 'x') and not (request.POST['alcohol'] == "yes" and i.alcohol == 'x') and not (request.POST['rxotc'] == "otc" and i.rx_otc == 'rx') and not (request.POST['csa'] == "no" and i.csa == '4'):
            score = (7*m + i.rating*i.popularity)/(i.popularity+7)
            drug_name = i.drug_name
            t = (score, drug_name)
            temp_list.append(t)
    sorted_list = sorted(temp_list, key= lambda d:d[0], reverse=True)


    if len(sorted_list) == 0 or len(sorted_list[0]) == 0:
        return HttpResponse("Sorry. No suitable recommendation for you.")
    drug_result = sorted_list[0][1]
    history_set.add(drug_result)

    template = loader.get_template('drugweb/result.html')
    context = {
        'drug_result': drug_result,
        'drug_details': get_object_or_404(Drugdetails, drug_name = drug_result)
    }
    return HttpResponse(template.render(context,request))

def weightedAverage():
    sum = 0
    pop = 0
    all_list = list(Cure.objects.all())
    for i in all_list:
        sum += i.popularity * i.rating
        pop += i.popularity
    return sum/pop

def score(s):
    return s['score']