from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'ashd389sh'})

def password(request):
	charecters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercaser'):
		charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('specials'):
		charecters.extend(list('!@#$%^&*()_+'))

	if request.GET.get('numbers'):
		charecters.extend(list('1234567890'))	

	length = int(request.GET.get('length',8))
	thepassword = ''
	for i in range(length):
		thepassword += random.choice(charecters)

	return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
	return render(request, 'generator/about.html')	