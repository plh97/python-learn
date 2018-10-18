

# #!/usr/bin/python

# # -*- coding: UTF-8 -*-
# 算出0-n以内的素数


def isPrime(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True



limit=int(input("素数范围>>>>"))
i = 2
nums = []
max = 0
while i < limit:
    if(isPrime(i)):
        # nums.append(i)
        max = i
        print(max)
        # print(nums)
    i+=1
