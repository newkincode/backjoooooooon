N = int(input())
if N != 5:
    KOREA, MATH, ENG, QUEST = map(int, input().split())
    THE2 = 0
else:
    KOREA, MATH, ENG, QUEST, THE2 = map(int, input().split())

# 국어점수가 영어 점수보다 높다면 두 점수의 차에 508을 곱해준다. if else 두 점수의 차에 108을 곱해준다

# 국어점수 > 영어점수: (|국어점수-영어점수|) * 508
# else: (|국어점수-영어점수|) * 108
# A

# 수학점수 > 탐구점수: (|수학점수-영어점수|) * 212
# else: (|수학점수-영어점수|) * 305
# B

# if N == 5:
# 제2외국어점수 * 707
# C

# (A + B + C) * 04763

if KOREA > ENG:
    A = abs(KOREA-ENG) * 508
else:
    A = abs(KOREA-ENG) * 108

if MATH > QUEST:
    B = abs(MATH-ENG) * 212
else:
    B = abs(MATH-ENG) * 212

C = THE2 * 707

print((A+B+C) * 4763)