from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from ReLearn.forms import UserSearchForm
from ReLearn.forms import SignupForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import ReLearn

import pymysql
import json

def account(request):
  return JsonResponse(
      {
        "name": "testuser",
        "type": "student"
        }
  )

def helloworld(request):
    return HttpResponse("Hello, world. This is a test view - Basic http response.")

def thanks(request):
    return HttpResponse("Thank you for adding to our database!")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # insertdata processing code
            # and redirect to a new URL
            sendToDatabase(int(form.data['user_type']), form)
            return HttpResponseRedirect('/thanks/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def getusers(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            # insertdata processing code
            # and redirect to a new URL
            print(json.dumps(form.data))
            jsonRes = matchPeople(int(form.data['user_type']), form)
            return JsonResponse(jsonRes)
    else:
        form = UserSearchForm()
    return render(request, 'findusers.html', {'form': form})

def sendToDatabase (person, form):
    if person == 1:
        connection = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='ReLearn2015',
                                    db='Students')

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO entries (studentName, personalityType, description) values (\"{}\", \"{}\", \"{}\");".format(form.data['user_name'], form.data['user_personality'], form.data['user_writeup'])
                cursor.execute(sql)
                # sql = "SELECT * FROM entries"
                # cursor.execute(sql)
                # result = cursor.fetchall()
                # print(result)
        finally:
            connection.commit()
            connection.close()
    elif person == 2:
        connection = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='ReLearn2015',
                                    db='Tutors')

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO entries (tutorName, personalityType, description) values (\"{}\", \"{}\", \"{}\");".format(form.data['user_name'], form.data['user_personality'], form.data['user_writeup'])
                cursor.execute(sql)
                # sql = "SELECT * FROM entries"
                # cursor.execute(sql)
                # result = cursor.fetchall()
                # print(result)
        finally:
            connection.commit()
            connection.close()

def matchPeople(person, form):
    matrix = {'ISTJISTJ': 1, 'ISTJISFJ': 1, 'ISTJINTP': 0.5, 'ISTJISFP': 0.5, 'ISTJINFJ': 0, 'ISTJINTJ': 0.5, 'ISTJISTP': 0.5, 'ISTJINFP': 0, 'ISTJESTP': 1, 'ISTJENFP': 0, 'ISTJESFP': 1, 
    'ISTJENTP': 0.5, 'ISTJESTJ': 1, 'ISTJESFJ': 1, 'ISTJENFJ': 0, 'ISTJENTJ': 0.5, 'ISFJISTJ': 1, 'ISFJISFJ': 1, 'ISFJINTP': 0.5, 'ISFJISFP': 0.5, 'ISFJINFJ': 0, 'ISFJINTJ': 0.5, 'ISFJISTP': 0.5, 
    'ISFJINFP': 0, 'ISFJESTP': 1, 'ISFJENFP': 0, 'ISFJESFP': 1, 'ISFJENTP': 0.5, 'ISFJESTJ': 1, 'ISFJESFJ': 1, 'ISFJENFJ': 0, 'ISFJENTJ': 0.5, 'INTPISTJ': 0.5, 'INTPISFJ': 0.5, 'INTPINTP': 1, 
    'INTPISFP': 0.5, 'INTPINFJ': 1, 'INTPINTJ': 1, 'INTPISTP': 0.5, 'INTPINFP': 1, 'INTPESTP': 0.5, 'INTPENFP': 1, 'INTPESFP': 0.5, 'INTPENTP': 1, 'INTPESTJ': 1, 'INTPESFJ': 0.5, 'INTPENFJ': 1, 
    'INTPENTJ': 1, 'ISFPISTJ': 0.5, 'ISFPISFJ': 0.5, 'ISFPINTP': 0.5, 'ISFPISFP': 0.5, 'ISFPINFJ': 0, 'ISFPINTJ': 0.5, 'ISFPISTP': 0.5, 'ISFPINFP': 0, 'ISFPESTP': 0.5, 'ISFPENFP': 0, 
    'ISFPESFP': 0.5, 'ISFPENTP': 0.5, 'ISFPESTJ': 1, 'ISFPESFJ': 1, 'ISFPENFJ': 1, 'ISFPENTJ': 0.5, 'INFJISTJ': 0.5, 'INFJISFJ': 0.5, 'INFJINTP': 1, 'INFJISFP': 0.5, 'INFJINFJ': 1, 
    'INFJINTJ': 1, 'INFJISTP': 0.5, 'INFJINFP': 1, 'INFJESTP': 0.5, 'INFJENFP': 1, 'INFJESFP': 0.5, 'INFJENTP': 1, 'INFJESTJ': 0.5, 'INFJESFJ': 0.5, 'INFJENFJ': 1, 'INFJENTJ': 1, 
    'INTJISTJ': 0.5, 'INTJISFJ': 0.5, 'INTJINTP': 1, 'INTJISFP': 0.5, 'INTJINFJ': 1, 'INTJINTJ': 1, 'INTJISTP': 0.5, 'INTJINFP': 1, 'INTJESTP': 0.5, 'INTJENFP': 1, 'INTJESFP': 0.5, 
    'INTJENTP': 1, 'INTJESTJ': 0.5, 'INTJESFJ': 0.5, 'INTJENFJ': 1, 'INTJENTJ': 1, 'ISTPISTJ': 0.5, 'ISTPISFJ': 0.5, 'ISTPINTP': 0.5, 'ISTPISFP': 0.5, 'ISTPINFJ': 0, 'ISTPINTJ': 0.5, 
    'ISTPISTP': 0.5, 'ISTPINFP': 0, 'ISTPESTP': 0.5, 'ISTPENFP': 0, 'ISTPESFP': 0.5, 'ISTPENTP': 0.5, 'ISTPESTJ': 1, 'ISTPESFJ': 1, 'ISTPENFJ': 0, 'ISTPENTJ': 0.5, 'INFPISTJ': 0.5, 
    'INFPISFJ': 0.5, 'INFPINTP': 1, 'INFPISFP': 0.5, 'INFPINFJ': 1, 'INFPINTJ': 1, 'INFPISTP': 0.5, 'INFPINFP': 1, 'INFPESTP': 0.5, 'INFPENFP': 1, 'INFPESFP': 0.5, 'INFPENTP': 1, 
    'INFPESTJ': 0.5, 'INFPESFJ': 0.5, 'INFPENFJ': 1, 'INFPENTJ': 1, 'ESTPISTJ': 1, 'ESTPISFJ': 1, 'ESTPINTP': 0.5, 'ESTPISFP': 0.5, 'ESTPINFJ': 0, 'ESTPINTJ': 0.5, 'ESTPISTP': 0.5, 
    'ESTPINFP': 0, 'ESTPESTP': 0.5, 'ESTPENFP': 0, 'ESTPESFP': 0.5, 'ESTPENTP': 0.5, 'ESTPESTJ': 0.5, 'ESTPESFJ': 0.5, 'ESTPENFJ': 0, 'ESTPENTJ': 0.5, 'ENFPISTJ': 0.5, 'ENFPISFJ': 0.5, 
    'ENFPINTP': 1, 'ENFPISFP': 0.5, 'ENFPINFJ': 1, 'ENFPINTJ': 1, 'ENFPISTP': 0.5, 'ENFPINFP': 1, 'ENFPESTP': 0.5, 'ENFPENFP': 1, 'ENFPESFP': 0.5, 'ENFPENTP': 1, 'ENFPESTJ': 0.5, 
    'ENFPESFJ': 0.5, 'ENFPENFJ': 1, 'ENFPENTJ': 1, 'ESFPISTJ': 1, 'ESFPISFJ': 1, 'ESFPINTP': 0.5, 'ESFPISFP': 0.5, 'ESFPINFJ': 0, 'ESFPINTJ': 0.5, 'ESFPISTP': 0.5, 'ESFPINFP': 0, 
    'ESFPESTP': 0.5, 'ESFPENFP': 0, 'ESFPESFP': 0.5, 'ESFPENTP': 0.5, 'ESFPESTJ': 0.5, 'ESFPESFJ': 0.5, 'ESFPENFJ': 0, 'ESFPENTJ': 0.5, 'ENTPISTJ': 0.5, 'ENTPISFJ': 0.5, 'ENTPINTP': 1, 
    'ENTPISFP': 0.5, 'ENTPINFJ': 1, 'ENTPINTJ': 1, 'ENTPISTP': 0.5, 'ENTPINFP': 1, 'ENTPESTP': 0.5, 'ENTPENFP': 1, 'ENTPESFP': 0.5, 'ENTPENTP': 1, 'ENTPESTJ': 0.5, 'ENTPESFJ': 0.5, 
    'ENTPENFJ': 1, 'ENTPENTJ': 1, 'ESTJISTJ': 1, 'ESTJISFJ': 1, 'ESTJINTP': 1, 'ESTJISFP': 1, 'ESTJINFJ': 0, 'ESTJINTJ': 0.5, 'ESTJISTP': 1, 'ESTJINFP': 0, 'ESTJESTP': 0.5, 'ESTJENFP': 0, 
    'ESTJESFP': 0.5, 'ESTJENTP': 0.5, 'ESTJESTJ': 1, 'ESTJESFJ': 1, 'ESTJENFJ': 0, 'ESTJENTJ': 0.5, 'ESFJISTJ': 1, 'ESFJISFJ': 1, 'ESFJINTP': 0.5, 'ESFJISFP': 1, 'ESFJINFJ': 0, 'ESFJINTJ': 0.5, 
    'ESFJISTP': 1, 'ESFJINFP': 0, 'ESFJESTP': 0.5, 'ESFJENFP': 0, 'ESFJESFP': 0.5, 'ESFJENTP': 0.5, 'ESFJESTJ': 1, 'ESFJESFJ': 1, 'ESFJENFJ': 0, 'ESFJENTJ': 0.5, 'ENFJISTJ': 0.5, 'ENFJISFJ': 0.5, 
    'ENFJINTP': 1, 'ENFJISFP': 1, 'ENFJINFJ': 1, 'ENFJINTJ': 1, 'ENFJISTP': 0.5, 'ENFJINFP': 1, 'ENFJESTP': 0.5, 'ENFJENFP': 1, 'ENFJESFP': 0.5, 'ENFJENTP': 1, 'ENFJESTJ': 0.5, 'ENFJESFJ': 0.5, 
    'ENFJENFJ': 1, 'ENFJENTJ': 1, 'ENTJISTJ': 0.5, 'ENTJISFJ': 0.5, 'ENTJINTP': 1, 'ENTJISFP': 0.5, 'ENTJINFJ': 1, 'ENTJINTJ': 1, 'ENTJISTP': 0.5, 'ENTJINFP': 1, 'ENTJESTP': 0.5, 'ENTJENFP': 1, 
    'ENTJESFP': 0.5, 'ENTJENTP': 1, 'ENTJESTJ': 0.5, 'ENTJESFJ': 0.5, 'ENTJENFJ': 1, 'ENTJENTJ': 1}
    
    preferred = []
    alright = []

    jsonResults = {}

    if person == 2: # Looking for Student
        connection = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='ReLearn2015',
                                    db='Tutors')

        results = [key for key in matrix if form.data['user_personality'] in key]
        for res in results:
            if matrix.get(res) == 1:
                if not (res.replace(form.data['user_personality'], "") in preferred) and not (len(res.replace(form.data['user_personality'], "")) == 0):
                    preferred.append(res.replace(form.data['user_personality'], ""))
                if len(res.replace(form.data['user_personality'], "")) == 0:
                    preferred.append(form.data['user_personality'])

            # elif matrix.get(res) == 0.5:

            #     if not (res.replace(form.data['user_personality'], "") in alright) and not (len(res.replace(form.data['user_personality'], "")) == 0):
            #         alright.append(res.replace(form.data['user_personality'], ""))
            #     if len(res.replace(form.data['user_personality'], "")) == 0:
            #         alright.append(form.data['user_personality'])
        
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM entries WHERE " #personalityType = \"" + form.data['user_personality'] + "\""
                for p in preferred:
                    sql += "personalityType = \"" + p + "\""
                    if preferred.index(p) != (len(preferred) - 1):
                        sql += " OR "
                
                cursor.execute(sql)
                result = cursor.fetchall()
                student = 0
                for r in result:
                    name, mb, desc, id = r
                    pDict = {"user_name": name, "user_personality": mb, "user_writeup": desc}
                    jsonResults[student] = pDict
                    student += 1

                return jsonResults
        finally:
            connection.close()

    elif person == 1: # Looking for Tutor
        connection = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password='ReLearn2015',
                                    db='Students')

        results = [key for key in matrix if form.data['user_personality'] in key]
        for res in results:
            if matrix.get(res) == 1:
                if not (res.replace(form.data['user_personality'], "") in preferred) and not (len(res.replace(form.data['user_personality'], "")) == 0):
                    preferred.append(res.replace(form.data['user_personality'], ""))
                if len(res.replace(form.data['user_personality'], "")) == 0:
                    preferred.append(form.data['user_personality'])

            # elif matrix.get(res) == 0.5:

            #     if not (res.replace(form.data['user_personality'], "") in alright) and not (len(res.replace(form.data['user_personality'], "")) == 0):
            #         alright.append(res.replace(form.data['user_personality'], ""))
            #     if len(res.replace(form.data['user_personality'], "")) == 0:
            #         alright.append(form.data['user_personality'])
        
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM entries WHERE " #personalityType = \"" + form.data['user_personality'] + "\""
                for p in preferred:
                    sql += "personalityType = \"" + p + "\""
                    if preferred.index(p) != (len(preferred) - 1):
                        sql += " OR "
                
                cursor.execute(sql)
                result = cursor.fetchall()
                student = 0
                for r in result:
                    name, mb, desc, id = r
                    pDict = {"user_name": name, "user_personality": mb, "user_writeup": desc}
                    jsonResults[student] = pDict
                    student += 1

                return jsonResults
        finally:
            connection.close()
