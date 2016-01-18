from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from WebServices.models import Company, Servers

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the WebServices index.")


def search_form(request):
    return render(request, 'search_form.html')
    

def search(request):
    if 'q' in request.GET and request.GET['q']:
    	choice = request.GET['choice']
        q = request.GET['q']
        if choice == 'Company':
	        companies = Company.objects.filter(Q(name__icontains=q)|Q(address__icontains=q))
	        servers = Servers.objects.order_by('preco')
	        return render(request, 'search_results.html',
	            {'companies': companies, 'query': q,
	            'servers':servers})
    	
    	if choice == 'CPU':
    		servers= Servers.objects.filter(Q(cpu__icontains=q)).order_by('preco')
    		return render(request,'search_results.html',
    			{'servers':servers,'query':q})
    	
    	if choice == 'HD':
    		servers= Servers.objects.filter(Q(disco__icontains=q)).order_by('preco')
    		return render(request,'search_results.html',
    			{'servers':servers,'query':q})
    	
    	if choice == 'Memory':
    		servers= Servers.objects.filter(Q(memoria__icontains=q)).order_by('preco')
    		servers.objects.order_by('preco')
    		return render(request,'search_results.html',
    			{'servers':servers,'query':q})
    else:
    	companies = Company.objects.all()
    	servers = Servers.objects.all().order_by('preco')
        return render(request, 'search_results.html',
            {'companies': companies,
            'servers':servers})


