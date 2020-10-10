from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from ReLearn.forms import SignupForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pymysql

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
                sql = "SELECT * FROM entries"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
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
                sql = "SELECT * FROM entries"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
        finally:
            connection.commit()
            connection.close()