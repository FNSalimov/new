from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.middleware import csrf
from restourant.models import Dish
import json

def index(request):
	return HttpResponse("Hey, how are you?")

def login(request):
	if request.method == "POST":
		ulogin = request.POST.get('login', '')
		upassword = request.POST.get('password', '')
		user = auth.authenticate(username=ulogin, password=upassword)
		if user is not None:
			auth.login(request, user)
			return HttpResponse('{"result": true}', content_type='application/json')
		else:
			return HttpResponse('{"result": false, "error": "There is no such user"}', content_type='application/json')
	elif request.method == "GET":
		return HttpResponse(csrf.get_token(request))

def menu(request):
	if request.user.is_authenticated:
		dishes = list(Dish.objects.all())
		jsonStr = json.dumps([d.toJSON() for d in dishes], ensure_ascii=False)
		return HttpResponse(jsonStr, content_type='application/json')

	return HttpResponse("Your are not authenticated")