from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def articles_by_year(request, year):
    return HttpResponse(f'''
        {year}년도에 대한 목록
    ''')


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

#blog/hello_times/10/ 으로 요청으면 10번 출력
def hello_times(request, times):
    message ="<font color = 'BLUE'>"
    message = message + "안녕하세요?  " * times
    message = message + "</font>"
    return HttpResponse(message)

#Naver 실시간 검색 결과
def naver_realtime_keywords(request):
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')
    text = '<br/>\n'.join([tag.text for tag in tag_list])
    return HttpResponse(text)
