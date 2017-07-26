from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.middleware import csrf
from restourant.models import Dish, Order
import json
from django.utils import timezone

def index(request):
	print(Order.objects.get(id=1).time)
	return HttpResponse("Hey, how are you?")

def login(request):
	if request.method == "POST":
		t = request.POST.get('t')
		t = t.split(',')
		for i in t:
			print(i)
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

def order(request):
	if request.method == "POST":
		order = Order(operator=request.POST.get('operator'), time=timezone.now(), restor_name=request.POST.get('restor'))
		dishes = request.POST.get('dishes')
		dishes = [int(d) for d in dishes.split(',')]
		print(dishes)
		for d in dishes:
			dish = Dish.objects.get(id=d)
			order.total_price += dish.price
		order.save()
		print(order.total_price)
		jsonStr = json.dumps({'total_price': order.total_price})
		return HttpResponse(jsonStr, content_type='application/json')
	elif request.method == "GET":
		return HttpResponse(csrf.get_token(request))