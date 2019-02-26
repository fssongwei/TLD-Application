from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from models import test_data
from models import Plane
from models import Metadata

from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
import requests 
import hashlib
import re


def index(request):

	#test_data.objects.all().delete()

	if request.method=='GET':
		plane=request.GET.get('plane',default='0')

	#block = 11
	#f = requests.get("https://s3-us-west-1.amazonaws.com/tld.cloud/ECFR_1hour_data_dump.txt")
	#f = f.text
	#datas = re.findall('\[(.*?)\]', f)

	#pk = 1
	#for tmp_data in datas:
	#	if pk > 20:
	#		break
	#	cloudMD5 = hashlib.md5()   
	#	cloudMD5.update(tmp_data)   
	#	cloudMD5 = cloudMD5.hexdigest()

	#	test_data.objects.create(id = pk, data = tmp_data, blocknum = 11, MD5 = cloudMD5)
	#	pk = pk + 1

	PlaneInfo = Plane.objects.all()


	TLDdata=test_data.objects.all()
	#for id in TLDdata:
	#	id.variables = id.data.split(",")
	#	m2 = hashlib.md5()   
	#	m2.update(id.data)
	#	id.localMD5 = m2.hexdigest()
	#	id.f = f
	
	return render(request, 'TLD/index.html', locals())
	#return render_to_response("TLD/index.html",locals())

def tableview(request):

	TLDdata=test_data.objects.filter(blocknum="11")[:50]
	meta_data = Metadata.objects.filter(blockID="11")

	for id in TLDdata:
		id.variables = id.data.split(",")
		m2 = hashlib.md5()   
		m2.update(id.data)
		id.localMD5 = m2.hexdigest()

	if request.method=='GET':
		plane=request.GET.get('plane',default='0')

	return render(request, 'TLD/tableview.html', locals())

def chartview(request):

	TLDdata=test_data.objects.filter(blocknum="11")[:50]
	meta_data = Metadata.objects.filter(blockID="11")

	label = " "
	oilPressure = ""
	oilTemperature = ""
	for id in TLDdata:
		variables = id.data.split(",")
		oilPressure = oilPressure + variables[12] + ","
		oilTemperature = oilTemperature + variables[11] + ","
		label = label + ","

	if request.method=='GET':
		plane=request.GET.get('plane',default='0')

	return render(request, 'TLD/chartview.html', locals())

def dataprocess(request):

	if request.method=='GET':
		plane=request.GET.get('plane',default='0')

	test_data.objects.all().delete()

	file = requests.get("https://s3-us-west-1.amazonaws.com/tld.cloud/ECFR_1hour_data_dump.txt")
	file = file.text

	rawdata = file.split("\n")
	#datas = re.findall('\[(.*?)\]', file)

	blockId = 11

	tid = 1
	for row in rawdata:
		if tid < 100:
			if row[0] == ".":
				fields = row.split(" ")
				blockId = fields[1]
			else:
				row = row.replace("[", "")
				row = row.replace("]", "")
				cloudMD5 = hashlib.md5()
				cloudMD5.update(row)   
				cloudMD5 = cloudMD5.hexdigest()

				test_data.objects.create(id = tid, data = row, blocknum = blockId, MD5 = cloudMD5)
				tid = tid + 1

	return render(request, 'TLD/dataprocess.html', locals())

