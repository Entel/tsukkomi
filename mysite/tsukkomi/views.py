from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from tsukkomi.models import *
import datetime

# Create your views here.
def tsukkomi_index(request):
	content_list = Content.objects.all().order_by('-time')[:5]
		
	return render_to_response('tsukkomi/index.html', 
					{'content_list': content_list},
					 RequestContext(request))

def tsukkomi_submit(request):
	content_list = Content.objects.all().order_by('-time')[:5]
	errors = []
	if request.method == 'POST':
		if not request.POST.get('content', ''):
			errors.append('Enter a subject')
		if not errors:
			insert = Content(text = request.POST['content'], 
					time = datetime.datetime.now(),
					ip = get_client_ip(request))
			insert.save()
			print(request.POST['content'])
			return HttpResponseRedirect('tsukkomi/')
	print(errors)
	return HttpResponseRedirect('/tsukkomi/')
	'''
	return render_to_response('tsukkomi/index.html', 
					{'content_list': content_list},
					 RequestContext(request))
'''

def showComment(request):
	comment_list = Content.objects.all().order_by('-time')[:5]
	

#get user ip
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

