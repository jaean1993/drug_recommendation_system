from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from operator import attrgetter
# Create your views here.

from .models import Cure, Drugdetails
history_set = set()
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


    for i in query_list:
        if i.drug_name not in history_set and not(request.POST['pregnancy'] == "yes" and i.pregnancy == 'x') and not (request.POST['alcohol'] == "yes" and i.ALCOHOL == 'x') and not (request.POST['rxotc'] == "otc" and i.RX_OTC == 'rx') and not (request.POST['csa'] == "no" and i.CSA == '4'):
            drug_result = i.drug_name
            break
    if len(drug_result) == 0:
        return HttpResponse("Sorry. No suitable recommendation for you.")

    history_set.add(drug_result)

    template = loader.get_template('drugweb/result.html')
    context = {
        'drug_result': drug_result,
        'drug_details': get_object_or_404(Drugdetails, drug_name = drug_result)
    }
    return HttpResponse(template.render(context,request))
