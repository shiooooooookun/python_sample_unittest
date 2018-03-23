#coding:utf-8

def add_num(num1,num2):
    return num1+num2

def minus_num(num1,num2):
    return num1-num2

def multi_num(num1,num2):
    return num1*num2

def devise_num(num1,num2):
    if num1 == 0 or num2 == 0: return False
        return num1%num2

def is_positive(num):
    return num > 0

def is_minus(num):
    return num < 0

def linear_search(arr,index):
    for i in range(len(arr)):
        if arr[i] == index: return True
    return False

