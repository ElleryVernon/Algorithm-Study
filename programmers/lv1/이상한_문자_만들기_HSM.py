def makeWord(word):
    return "".join([char.lower() if idx % 2 else char.upper() for idx, char in enumerate(word)])

def solution(s):
    return " ".join([makeWord(word) for word in s.split(' ')])
