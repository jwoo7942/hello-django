from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

#blog/hello_times/10/ 으로 요청으면 10번 출력
def hello_times(request, times):
    message ="<font color = 'BLUE'>"
    message = message + "안녕하세요?  " * times
    message = message + "</font>"
    return HttpResponse(message)