### python 游戏编程入门

###### 还是学习一下 python 这一门 ooop 语言吧.

#### python OOP: Python 的方式

- 多态
  指具备多种形态的功能

- 数据隐藏(封装)
  python 不允许变量声明为私有或者隐藏,事实上 python 没有私有变量,但是通过下面函数可实现简单封装
  ```python
  def GetDistance(self):
      return p_distance
  def SetDistance(self, value):
      p_distance = value
  ```

- 继承
  ```python
  class Car(Vehicle):
  ```
  子类中可以使用super()引用基类
  此外,python可以实现多继承,也就是说一个子类可以继承自多个父类或者基类
  ```python
    class Car(Body, Engine, Suspension, Interior):
  ```
  只要每个父类中的变量和方法与其他变量和方法不冲突,新的子类可以访问他们毫无问题.但是,