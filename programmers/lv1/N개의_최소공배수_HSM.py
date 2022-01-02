from functools import reduce

def getGcd(num1, num2):
    return getGcd(num2, num1 % num2) if num2 else num1

def getGcm(num1, num2):
    return num1 * num2 / getGcd(num1, num2)

def solution(arr):
    return reduce(lambda acc, cur: getGcm(acc, cur), arr)
