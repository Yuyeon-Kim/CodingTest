from math import gcd
def solution(w,h):
    return w*h-w-h+gcd(w,h) # w * h - (w/gcd(w, h) + h/gcd(w, h) - 1) * gcd(w, h)
    # w/gcd(w, h) : 작은 사각형의 가로
    # h/gcd(w, h) : 작은 사각형의 세로
    # w/gcd(w, h) + h/gcd(w, h) - 1 : 작은 사각형에서 나눠지는 사각형의 수
    # (왜? 왼쪽, 오른쪽으로 나눠지는 사각형을 밀었을 때 ㄱ자 모양이 나옴)
    # * gcd(w, h) : 작은 사각형이 있는 개수