from django.shortcuts import render

from models import data
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response

import hashlib


def index(request):
	TLDdata=data.objects.all()
	MD5 = []
	for id in TLDdata:
		m2 = hashlib.md5()   
		m2.update(id.TLDdata)   
		id.localMD5 = m2.hexdigest()

	return render(request, 'TLD/index.html', locals())
	#return render_to_response("TLD/index.html",locals())