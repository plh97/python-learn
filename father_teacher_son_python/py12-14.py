# 不可改变的数组


one = input(">>")
two = input(">>")
three = input(">>")
four = input(">>")
five = input(">>")


arr = [one,two,three,four,five]


def printRes(arr):
    res='The names are '
    for i in arr:
        res+=i+' '
    print(res)

printRes(arr)

which = input('need to replace which one?')

val = input('new name?')

arr[int(which)] = val

printRes(arr)
