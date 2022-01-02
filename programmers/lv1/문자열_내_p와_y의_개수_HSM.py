def count(iterable, target):
    cnt = 0
    for item in iterable:
        if item == target:
            count += 1
    return cnt
            

def solution(s):
    return count(s.lower(), "y") == count(s.lower(), "p")
