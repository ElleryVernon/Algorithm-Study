def solution(num):
    return sum([cur for cur in range(1, num // 2 + 1) if num % cur == 0]) + num
