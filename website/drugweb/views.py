from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from operator import attrgetter
# Create your views here.

from .models import Cure, Drugdetails

def index(request):
    template = loader.get_template('drugweb/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
def result(request):
    post_cur_drug = request.POST['cur_drug']
    post_illness_name = request.POST['illness_name']

    #temp algorithm
    query_list = list(Cure.objects.filter(illness_name__contains=post_illness_name))

    if len(query_list) == 0:
        return HttpResponse("Sorry. No suitable recommendation for you.")
    drug_result = ""

    query_list = sorted(query_list,key = attrgetter("popularity"), reverse= True)

    for i in query_list:
        if i.drug_name != post_cur_drug and not(request.POST['pregnancy'] == "yes" and i.pregnancy == 'x'):
            drug_result = i.drug_name
            break

    template = loader.get_template('drugweb/result.html')

    context = {
        'drug_result': drug_result,
        'drug_details': get_object_or_404(Drugdetails, drug_name = drug_result)
    }
    return HttpResponse(template.render(context,request))
