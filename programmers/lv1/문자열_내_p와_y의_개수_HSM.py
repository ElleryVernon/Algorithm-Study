# 너무 휑해서 카운터함수 만들어봄. 내장으로도 
def count(iterable, target):
    cnt = 0
    for item in iterable:
        if item == target:
            cnt += 1
    return cnt
            

def solution(s):
    return count(s.lower(), "y") == count(s.lower(), "p")
