from re import match 

def solution(s):
    return bool(match("^\d{6}$|^\d{4}$", s))
