## 父与子的编程之旅-与小卡特一起学python 阅读笔记&&习题练习

### python 可能出现的错误

#### syntax error
```python
print('Hoell')
print(Hoell')
```

#### runtime error
```python
print('Hoell')
print('Hoell' + 5)
```

##### 错误如下
```bash
python article1.py
  File "article1.py", line 7
    print(I'm full." + 5)
                        ^
SyntaxError: EOL while scanning string literal
```


#### 解释
为什么语法错误,因为"必须一前一后包裹变量
```python
str='str'
num = 123
str+num  # 报错
```
就像是3个苹果+5条鳄鱼,结果等于8,但是这种结果毫无意义.

但是另外一种语法如下又可以

```python
print('str'*5)  # strstrstrstrstr
```

为什么呢,就好像  2个苹果*2倍,就是4个苹果,这在数学上是有意义的.


