from django.shortcuts import render
from django.db import connection


# Create your views here.


def home(request):
	return render(request, 'home.html')

def index(request):
	#print request.GET
	exp = request.GET[u'pincode']
	#exp = request.GET[u'pincode'][0]
	
	result = my_custom_sql(exp)
	if result == []:
		result = "Wrong pincode"
	print result
	return render(request, 'index.html', {'result':result})

def my_custom_sql(exp):
    cursor = connection.cursor()
    a = "select * from schools where field8='" + exp + "';"
    print a
    cursor.execute(a)
    row = cursor.fetchall()
    print len(row)
    return row