# 切片数组


a = [9,2,3,4,5,6,7]


new_a = a[:]   # 生成新数组
_a = a   # 指向同个数组
a.sort(reverse=True)
print(new_a == a)

print(a)
print(_a)
print(new_a)