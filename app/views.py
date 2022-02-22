
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from multiprocessing import context
from django.shortcuts import render,redirect
from app.models import Company
import requests
from bs4 import BeautifulSoup as bs
import asyncio
import re
from datetime import time
import simplejson as json

def superUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request, "app/superuser.html",{"loggedIn":True,"updated":False})

    return render(request, "app/superuser.html",{"loggedIn":False,"updated":False})


def convertToList(string):
    jsonDecoder = json.decoder.JSONDecoder()
    return jsonDecoder.decode(string)

def convertToText(list):
    return json.dumps(list)

@login_required(login_url = 'superuser')
def update(request):

    companies = getAllCompaniesFromNepse()[:-1]   #removing the last empty company in the list

    companies_in_db = Company.objects.values('name')
    # converting string to list
    companies_in_db_list = convertToList((companies_in_db[0].get('name')))


    newly_added_companies = []

    for company in companies:
        if company not in companies_in_db_list:
            companies_in_db_list.append(company)
            newly_added_companies.append(company)


    # print(companies_in_db_list)
    old_companies_db = Company.objects.all()[0] 
    old_companies_db.name = convertToText(companies_in_db_list)
    old_companies_db.save()

    text_of_newly_added_companies = convertToText(newly_added_companies)

    return render(request, "app/superuser.html",{"loggedIn":True,"updated":True,"newly_added_companies":newly_added_companies})


def logoutUser(request):
    logout(request)
    return redirect('superuser')



def getAllCompaniesFromNepse():

    html_text = requests.get('http://www.nepalstock.com/').text

    soup = bs(html_text, 'lxml')

    data = soup.find('marquee').text
    data = data.split(')  ')

    companies = []

    for d in data:
        d = re.sub('[^A-Z]', '', d) # ^ represents that . remove all the characters except those characters present inside square brackets
        companies.append(d)

    return companies



def home(request):

    companies = Company.objects.all()

    companies_names_text = companies[0].name

    context = {
        "companies":convertToList(companies_names_text)
    }

    return render(request,'app/home.html',context)



