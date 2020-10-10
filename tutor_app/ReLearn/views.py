from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from ReLearn.forms import SignupForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def account(request):
  return JsonResponse(
      {
        "name": "testuser",
        "type": "student"
        }
  )

def helloworld(request):
    return HttpResponse("Hello, world. This is a test view - Basic http response.")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # insertdata processing code
            # and redirect to a new URL
            return HttpResponseRedirect('/thanks/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
