import json
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
import datetime
# Create your views here.

def api(request):
    now = datetime.datetime.now() 
    if request.method=="GET":
        X = request.GET.get('X')
        leaves = request.GET.get('leaves')
    response = {
        'earliestTime': solution(int(X),leaves),
        'datetime': f'{now}'
    }
    return HttpResponse(json.dumps(response), content_type='application/json')

def checkElementNotExceed(A,X):
    i = 0
    j = 0
    temp = 0
    for a in A:
        j = i + 1
        while j < len(A):
            if A[i] < A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
            j+=1
        i+=1
    print("A[0]",A[0])
    if A[0] <= X:
        return True
    else: 
        return False

def solution(X,Ar):
    print(Ar)
    leaves_str = Ar.replace("[","")
    leaves_str = leaves_str.replace("]","")
    leaves_array_str = leaves_str.split(",")
    leaves_array = []
    for leave in leaves_array_str:
        print(leave)
        leaves_array.append(int(leave))
    
    if X not in leaves_array:
        return -1

    result = 0
    k = 0 #time in seconds
    N = len(leaves_array) #represent falling leaves
    leaves = []
    if N >= 1 and N <= 100000:
        if X >= 1 and X <= 100000:
            if checkElementNotExceed(leaves_array,X):
                for a in leaves_array:
                    if a not in leaves:
                        leaves.append(a)
                        print("A[",k,"] = ",a)
                        result = k
                    k+=1
        else:
            result = "X out of bound" 
    else:
        result = "Max index out of bound"
    return result