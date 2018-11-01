### python 黑客攻防入门

#### 一个黑客至少掌握 3-4 种语言

- c 和汇编语言
  他在分析系统与进程中起着核心作用

* 工具语言
  python,有着众多的库支持黑客攻击,
  pydbg, scapy, sqlmap, httplib 等等
  可访问文件的 api

### 基础知识

- 黑客攻击技术
- 系统
- Python

++++++++++++++++++

### 实用黑客攻击技术

- 应用程序黑客攻击
- Web 黑客攻击
- 网络黑客攻击
- 系统黑客攻击

++++++++++++++++++

### 高级黑客知识

- 汇编语言
- 黑客攻击工具
- 逆向工

### web

目前来说大部分应用都是由 C/S(Client/Server)环境构成

#### 头部信息

| 字段             | 说明                                                            |
| :--------------: | :-------------------------------------------------------------: |
| Host             | 提供服务的服务器域名与 TCP 端口信息, Host: en.wikipidia.org:80 |
| User-agent       | 请求的客户端浏览器信息                                          |
| Accept-Encoding  | 可处理编码信息                                                  |
| Accept-Language  | 可处理语言,供人使用                                             |
| Referenece       | 从哪个网页请求的信息                                            |
| Cookie           | 存储信息                                                        |
| Status           | 状态码                                                          |
| Date             | 时间                                                            |
| Server           | 服务器系统信息                                                  |
| Content-Type     | 相应数据 Type 信息                                              |
| Content-Encoding | 相应编码信息:Gzip                                               |
| Set-Cooking      | 客户端保存的 Cookie                                             |
| Cache-Control    | 使用缓存,设置缓存生命周期,秒单位                                |
| Connection       |  处理响应后,设置对连接的处理                                   |
| Content-Length   | Http 相应体的长度,以字节 (8 bytes) 位单位                      |


### python 保留字
| keyword  | 说明                       |
| :------: | :------------------------: |
| and      | &&与逻辑                   |
| del      | 删除                       |
| for      | 循环                       |
| is       | 是                         |
| raise    | 允许python强制发生指定异常 |
| assert   | 断言                       |
| elif     | 或者如果                   |
| form     | 表格                       |
| lambda   | 方便用于解一些方程         |
| return   | 退出函数并返回             |
| break    | 断开                       |
| else     | 如果也                     |
| global   | 全局                       |
| not      | 不                        |
| try      | 尝试                      |
| class    | 类                        |
| except   | 期待                      |
| if       | 如果                      |
| or       | 或逻辑                    |
| while    | 当XXX的时候               |
| continue | 继续循环                  |
| exec     | 用于对字符串进行解析       |
| import   | 引入                       |
| pass     | 下一个                    |
| yield    | 迭代器                    |
| def      | 函数                      |
| finally  | try...expect...finally    |
| in       | for i in range(10)         |
| print    | 打印                       |




### 模块
- import 模块名
- import 模块名, 模块名
- from 模块名 import 函数名/属性名
- import 模块名 as 别名

### 字符串格式化
| code  | description | 格式             |
| :---: | :---------: | :-:             |
| %s    | 字符串       | String          |
| %c    | 单个字符      | Character       |
| %d    | 整数         | Integer           |
| %f    | 浮点数       | Floating Pointer   |
| %o    | 八进制数      | Octal Number      |
| %x    | 十六进制数    | Hexadecimal Number |



```py
print("print [%s]" % 'text')
print("print [%10s]" % 'text')
print("print [%c]" % 't')
print("print [%5c]" % 't')
print("print [%d]" % 123)
print("print [%f]" % 123)
print("print [%o]" % 123)
print("print [%x]" % 123)


# print [text]
# print [      text]
# print [t]
# print [    t]
# print [123]
# print [123.000000]
# print [173]
# print [7b]
```

### ctypes 库






### 最后

还是得学习 python 啊,c,java 搞不了,还是 python 把,JavaScript 页面工程太表层了额.期待有个环境,钱多事少,让我能在课余时间多学习...虽然还是菜.
