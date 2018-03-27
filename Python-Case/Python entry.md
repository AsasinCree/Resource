**Python**

#常用代码
 - guess = int(input('Enter an integer : '))
    - 内置的 input 函数提供一串打印到屏幕上的字符串并等待用户的输入。一旦我们输入了某些内容并按下键盘上的 enter 键， input() 函数将以字符串的形式返回我们所输入的内容
    - 通过 int 将这个字符串转换成一个整数并将其储存在变量 guess 中。实际上， int 是一个类（Class），但你现在你所需要知道的就是你可以使用它将一串字符串转换成一个整数（假设这个字符串的文本中含有一个有效的整数）
 - range(start, end, [step])
    - 不包含 end
    - range() 每次只会生成一个数字，如果你希望获得完整的数字列表，要在使用 range() 时调用 list() 。例如下面这样： list(range(5)) ，它将会返回 [0, 1, 2,3, 4]

Perl 语言中“总是有多种方法来做同一件事”的理念在Python开发者中通常是难以忍受的。Python开发者的哲学是“用一种方法，最好是只有一种方法来做一件事”。
Python开发人员尽量避开不成熟或者不重要的优化. 一些针对非重要部位的加快运行速度的补丁通常不会被合并到Python内。所以很多人认为Python很慢。不过，根据二八定律，大多数程序对速度要求不高。在某些对运行速度要求很高的情况，Python设计师倾向于使用JIT技术，或者用使用C/C++语言改写这部分程序。可用的JIT技术是PyPy(PyPy是用Python实现的Python解释器。 [动态编译器])。
Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。
Python在执行时，首先会将.py文件中的源代码编译成Python的byte code（字节码），然后再由Python Virtual Machine（Python虚拟机）来执行这些编译好的byte code。这种机制的基本思想跟Java，.NET是一致的。然而，Python Virtual Machine与Java或.NET的Virtual Machine不同的是，Python的Virtual Machine是一种更高级的Virtual Machine。这里的高级并不是通常意义上的高级，不是说Python的Virtual Machine比Java或.NET的功能更强大，而是说和Java 或.NET相比，Python的Virtual Machine距离真实机器的距离更远。或者可以这么说，Python的Virtual Machine是一种抽象层次更高的Virtual Machine。
Python 的底层是用 C 语言写的，很多标准库和第三方库也都是用 C 写的，运行速度非常快
Python既支持面向过程的编程也支持面向对象的编程。在“面向过程”的语言中，程序是由过程或仅仅是可重用代码的函数构建起来的。在“面向对象”的语言中，程序是由数据和功能组合而成的对象构建起来的
一个用编译性语言比如C或C++写的程序可以从源文件（即C或C++语言）转换到一个你的计算机使用的语言（二进制代码，即0和1）。这个过程通过编译器和不同的标记、选项完成。运行程序的时候，连接/转载器软件把你的程序从硬盘复制到内存中并且运行。而Python语言写的程序不需要编译成二进制代码。你可以直接从源代码运行 程序。在计算机内部，Python解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使用的机器语言并运行。这使得使用Python更加简单。也使得Python程序更加易于移植


控制语句
    pass语句。表示此行为空，不运行任何操作。
    def语句。用于定义函数和类型的方法
    with语句。Python2.6以后定义的语法，在一个场景中运行语句块。比如，运行语句块前加密，然后在语句块运行退出后解密。
    from import语句。从包导入模块或从模块导入某个对象。
    import as语句。将导入的对象赋值给一个变量。
    raise语句。制造一个错误。
表达式
    //, **, ~, % 整除、乘方、取补、取余
    ^ XOR; ~, |, ^, &, <<, >>必须应用于整数。
    Python使用and, or, not表示逻辑运算。
    is, is not用于比较两个变量是否是同一个对象。in, not in用于判断一个对象是否属于另外一个对象。
    Python支持“列表推导式”（list comprehension），比如计算0-9的平方和: >>> sum(x * x for x in range(10))
    Python使用lambda表示匿名函数。匿名函数体只能是表达式。比如：>>> add=lambda x, y : x + y
    Python使用y if cond else x表示条件表达式。意思是当cond为真时，表达式的值为y，否则表达式的值为x。相当于C++和Java里的cond?y:x。
    Python区分列表(list)和元组(tuple)两种类型。list的写法是[1,2,3]，而tuple的写法是(1,2,3)。可以改变list中的元素，而不能改变tuple。在某些情况下，tuple的括号可以省略。tuple对于赋值语句有特殊的处理。因此，可以同时赋值给多个变量
        比如：>>> x, y=1,2#同时给x,y赋值，最终结果：x=1, y=2
        特别地，可以使用以下这种形式来交换两个变量的值：>>> x, y=y, x #最终结果：y=1, x=2
    Python使用(单引号)和(双引号)来表示字符串。与Perl、Unix Shell语言或者Ruby、Groovy等语言不一样，两种符号作用相同。一般地，如果字符串中出现了双引号，就使用单引号来表示字符串;反之则使用双引号。如果都没有出现，就依个人喜好选择。出现在字符串中的\(反斜杠)被解释为特殊字符，比如\n表示换行符。表达式前加r指示Python不解释字符串中出现的\。这种写法通常用于编写正则表达式或者Windows文件路径。
函数 
    Python的函数支持递归、默认参数值、可变参数，但不支持函数重载。为了增强代码的可读性，可以在函数后书写“文档字符串”(Documentation Strings，或者简称docstrings)，用于解释函数的作用、参数的类型与意义、返回值类型与取值范围等。可以使用内置函数help()打印出函数的使用帮助
对象的方法
    instance.method(arguments)。它等价于调用Class.method(instance, arguments)        
    Python认识一些以“__”开始并以“__”结束的特殊方法名，它们用于实现运算符重载和实现多种特殊功能。
    当定义对象方法时，必须显式地定义第一个参数，一般该参数名都使用self，用于访问对象的内部数据。self与C++,Java里面的this不完全一样，它可以被看作是一个习惯性的用法，我们传入任何其它的合法名称都行。如下
        class User:
            def__init__(myself,name):
                myself.name=name
类型
    Python采用动态类型系统。在编译的时候，Python不会检查对象是否拥有被调用的方法或者属性，而是直至运行时，才做出检查。所以操作对象时可能会抛出异常。不过，虽然Python采用动态类型系统，它同时也是强类型的。Python禁止没有明确定义的操作，比如数字加字符串。
    Python允许程序员定义类型。类型本身也是特殊类型type的对象(type类型本身也是type对象)，这种特殊的设计允许对类型进行反射编程。
    数据类型
        str: 一个由字符组成的不可更改的有序串行。 'Wikipedia',"Wikipedia","""Spanning,multiple,lines"""
        bytes: 一个由字节组成的不可更改的有序串行。 b'Some ASCII',b"Some ASCII"
        list: 可以包含多种类型的可改变的有序串行  [4.0, 'string', True]
        tuple: 可以包含多种类型的不可改变的有序串行  (4.0, 'string', True)
        set, frozenset: 与数学中集合的概念类似。无序的、每个元素唯一。 {4.0, 'string', True}, frozenset([4.0, 'string', True])
        dict: 一个可改变的由键值对组成的无序串行。  {'key1': 1.0, 3: False}
        int: 精度不限的整数
        float: 浮点数。精度与系统相关。 3.1415927 
        complex: 复数 3+2.7j
        bool: 两个值：真、假
    除了各种数据类型，Python语言还用类型来表示函数、模块、类型本身、对象的方法、编译后的Python代码、运行时信息等等。因此，Python具备很强的动态性。
数学运算
    Python使用与C、Java类似的运算符，支持整数与浮点数的数学运算。同时还支持复数运算与无穷位数（实际受限于计算机的能力）的整数运算。除了求绝对值函数abs()外，大多数数学函数处于math和cmath模块内。前者用于实数运算，而后者用于复数运算
    fractions模块用于支持分数运算；decimal模块用于支持高精度的浮点数运算。
    Python定义求余运行a % b的值处于开区间[0, b)内，如果b是负数，开区间变为(b, 0]。为了让方程式：b * (a // b) + a % b = a恒真，整除运行需要向负无穷小方向取值。比如7 // 3的结果是2，而(-7) // 3的结果却是-3。这个算法与其它很多编程语言不一样，需要注意 (C# 为 -2)
    Python允许像数学的常用写法那样连着写两个比较运行符。比如a < b < c与a < b and b < c等价。C++的结果与Python不一样，首先它会先计算a < b，根据两者的大小获得0或者1两个值之一，然后再与c进行比较。
帮助
    用import导出模块 m 后，可使用函数dir(m)列出模块的所有函数
    查看完整的python内置函数清单: dir(_ _builtins_ _)
    查看某个函数的文档帮助信息 help(函数): help(sum)
CGI
    目前由NCSA维护，CGI(Common Gateway Interface)，通用网关接口，它是一段程序，运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。CGI程序可以是Python脚本、Perl脚本、Shell脚本、C或者C++程序等。 百度百科内容未全部摘录

一款软件开发流程:
1. What/做什么（分析）
2. How/怎么做（设计）
3. Do It/开始做（执行）
4. Test/测试（测试与修复错误）
5. Use/使用（操作或开发）
6. Maintain/维护（改进）

# 简明 Python 教程
## 基础
### 字符串
 - 三引号表示多行输入
 - 无 char 数据类型
 - 格式化方法
    1. print('{0} was {1} years old when he wrote this book'.format(name, age))  数字可省略
    2. print('{0:.3f}'.format(1.0/3))  # 对于浮点数 '0.333' 保留小数点(.)后三位
    3. print('{0:_^11}'.format('hello'))    # 使用下划线填充文本，并保持文字处于中间位置, 使用 (^) 定义 '___hello___'字符串长度为 11        
    4. print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))    # 基于关键词输出 'Swaroop wrote A Byte of Python'
    5. print 总是会以一个不可见的“新一行”字符（ \n ）结尾, 通过 end 指定其应以特定字符结尾  如 print('a', end='')
 - 转义序列
    1. 制表符 \t: 用来调整格式
    2. 字符串中一个放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行
 - 原始字符串: 字符串前加 r 或 R(正则表达式)
### 标志符命名
 - 首字符: 大小写 ASCII 字符或 Unicode 字符或下划线 _ , 其它字符可加上数字
 - 区分大小写
### 对象
 - Python 将程序中的任何内容统称为 对象（Object）。
 - 强（Strongly）面向对象的，所有的一切都是对象， 包括数字、字符串与函数
### 逻辑行与物理行
 - 物理行（Physical Line）是你在编写程序时 你所看到 的内容
 - 逻辑行（Logical Line）是 Python 所看到 的单个语句

## 运算符与表达式
### 运算符
 - 乘: 可返回字符串重复指定次数后的结果。eg: 'la' * 3 输出 'lalala'
 - 乘方 ****
 - // （整除）: x 除以 y 并对结果向下取整至最接近的整数。eg: -13 // 3 输出 -5
 - % （取模/余）: -25.5 % 2.25 输出 1.5 
 - ^ （按位异或）
 - ~ （按位取反）: x 的按位取反结果为 -(x+1). eg: ~5 输出 -6 
    - 前提
        - 计算机中负数都是用补码表示
        - x[补] = x[反] + 1
    - 过程: 
        1. 5 = 0101, 三bit能表示 -4~3; 4bit 能表示 -8~7; 5 在机器中至少需要 4 位(含1个符号位) 
        2. ~5 = 1010
            - 解法一: 此符号为1表示负数的补码; 根据公式求得5[反] = 1010 - 0001 = 1001, 5[原] = 1110(符号位不反转), 即 -6
            - 解法二: 补码的真值公式: 2幂之和(除了第一位符号位为减号). -1x2^3+0x2^2+1x2^1+0x2^0=-6
 - >,<,>=,<=
    - 可以任意组成组成链接: 3.2 < 5 < 7.0
    - 如果两个操作数均为数字，它们首先将会被转换至一种共同的类型。否则，它将总是返回 False
 - ==,!= 比较两个对象相等状态
 - not （布尔“非”）: x 为 false 或 0, not x = true
 - and （布尔“与”）: 支持短路计算（Short-circuit Evaluation）. x = False; y = True; x and y = False 计算过程不考虑 y
 - or （布尔“或”）: 支持短路计算
 - 数值运算与赋值的快捷方式
    - 对一个变量进行一项数学运算并将运算得出的结果返回给这个变量: 变量 运算 = 表达式
    - lambda ：Lambda 表达式
### 求值顺序
 - 有相同优先级的运算符将从左至右的方式依次进行求值
 - 优先级详细列表(优先级从低到高)
    1. if - else ：条件表达式
    2. or ：布尔“或”
    3. and ：布尔“与”
    4. not x ：布尔“非”
    5. in, not in, is, is not, <, <=, >, >=, !=, == ：比较，包括成员资格测试
    6. （Membership Tests）和身份测试（Identity Tests）。
    7. | ：按位或
    8. ^ ：按位异或
    9. & ：按位与
    10. <<, >> ：移动
    11. +, - ：加与减
    12. *, /, //, % ：乘、除、整除、取余
    13. +x, -x, ~x ：正、负、按位取反
    14. ** ：求幂
    15. x[index], x[index:index], x(arguments...), x.attribute ：下标、切片、调用、属性引用
    16. (expressions...), [expressions...], {key: value...}, {expressions...} ：显示绑定或数组、显示列表、显示字典、显示设置

## 控制流
### If
 - 学用 elif
 - 不管 if, elif, else 后都需要一个冒号来指定接下来会有一块语句在后头
 - Python 中不存在 switch 语句。你可以通过使用 if..elif..else 语句来实现同样的事情（在某些情况下，使用一部字典能够更快速地完成）
### while
 - 可加 else
### for
 - for i in range(0,5)   等同于   C/C++ for (int i = 0; i < 5; i++)
 - 可加 else: for 循环结束后开始执行
### break
 - 中断 for 或 while 循环，之中 else 块都将不会被执行
### continue

## 函数
函数（Functions）是指可重复使用的程序片段 
def function_name(paramter): 
content
### 函数参数
在定义函数 时给定的名称称作“形参”（Parameters），在调用函数时你所提供给函数的值称作“实 参”（Arguments）。
### 局部变量
当你在一个函数的定义中声明变量时，它们不会以任何方式与身处函数之外但具有相同名称的变量产生关系
### global 语句
如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还 是类），那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的.
```
a2=3 
def change3():
    global a2
    a2 = 2;
    print(a2)
```
### 默认参数值
对于一些函数来说，你可能为希望使一些参数可选并使用默认的值，以避免用户不想为他们提供值的情况
```
def default_parameter(message, times = 1):
    print(message * times)
```
只有那些位于参数列表末尾的参数才能被赋予默认参数值，意即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前。这是因为值是按参数所处的位置依次分配的.
### 关键字参数（Keyword Arguments）
如果你有一些具有许多参数的函数，而你又希望只对其中的一些进行指定，那么你可以通过 命名它们来给这些参数赋 
这样做有两大优点——其一，我们不再需要考虑参数的顺序，函数的使用将更加容易。其二，我们可以只对那些我们希望赋予的参数以赋值，只要其它的参数都具有默认参数值。
```
def keyword_argument(a, b=5, c=10):
    print('a is', a, 'b is', b, 'c is', c)

keyword_argument(1, 2)
keyword_argument(2, c=20)
keyword_argument(c=30, a=3)
```
### 可变参数
有时你可能想定义的函数里面能够有任意数量的变量，也就是参数数量是可变的，这可以通过使用星号来实现 
- 当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数 （Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。 
- 类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字 参数都将被收集并汇集成一个名为 param   的字典（Dictionary）
```
def various_argument(a, *numbers, **phonebook):
    print('a is', a)
    for number in numbers:
        print('signle_number:', number)
    for key, value in phonebook.items():
        print('key is', key, 'value is', value)

print(various_argument(11, 1,2,3, Jack=155, Sam=156, Law=157))
#外面一层 print 出来一个 None, 详见下一节 return
```
### return 语句
return 语句用于从函数中返回，也就是中断函数。我们也可以选择在中断函数时从函数中返回一个值。
return 语句没有搭配任何一个值则代表着 返回 None  。None 在 Python  中一 个特殊的类型，代表着虚无。举个例子，它用于指示一个变量没有值，如果有值则它的值便是 None（虚无）
每一个函数都在其末尾隐含了一句 return  None ，除非你写了你自己的 return 语句。你可 以运行 print(some_function()) ，其中 some_function 函数不使用 return 语句，就像这样：
```
def some_function():
    pass
```
Python 中的 pass 语句用于指示一个没有内容的语句
### DocStrings
文档字符串（Documentation Strings）能够帮助你更好地记录程序并让其更加易于理解。令人惊叹的是，当程序实际运行时，我们甚至可以通过一个函数来获取文档！ 
函数的第一行逻辑行中的字符串是该函数的文档字符串（DocString）。这里要注意文档字符串也适用于后面相关章节将提到的模块（Modules）与类（Class）  
该文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。 第二行为空行，后跟的第三行开始是任何详细的解释说明  
获取方式： 函数的 __doc__ 属性, help() 函数

## 模块
其中最简单的一种便是创建一个包含函数与变量、以 .py 为后缀的文件。  
另一种方法是使用撰写 Python 解释器本身的本地语言来编写模块。举例来说，你可以使用 C 语言来撰写 Python 模块，并且在编译后，你可以通过标准 Python 解释器在你的 Python 代码中使用它们  
```
import sys
print('The command line argument are:')
for i in sys.argv:
    print(i)

print('\n\nThe pythonpath is:', sys.path)
```
上述示例通过 cmd 命令执行: python module_using_sys.py we are arguments  
如果它不是一个已编译好的模块，即用 Python 编写的模块，那么 Python 解释器将从它的 sys.path 变量所提供的目录中进行搜索。如果找到了对应模块，则该模块中的语句将在开始 运行，并能够为你所使用。在这里需要注意的是，初始化工作只需在我们第一次导入模块时完成。  
sys.argv 变量是一系列字符串的列表（List）。具体而言， sys.argv 包含了命令行参数（Command Line Arguments）这一列表，也就是使用命令行传递给你的程序的参数。默认第一个参数为运行的脚本名称。  
sys.path 内包含了导入模块的字典名称列表。你能观察到 sys.path 的第一段字符串是空的——这一空字符串代表当前目录也是 sys.path 的一部分，它与 PYTHONPATH 环境变量等同。这意味着你可以直接导入位于当前目录的模块。否则，你必须将你的模块放置在 sys.path 内所列出的目录中
### 按字节码编译的 .pyc 文件
导入一个模块是一件代价高昂的事情。其中一种快速的方式便是创建按字节码编译的（Byte-Compiled）文件，这一文件以 .pyc 为其扩展名，是将 Python 转换成中间形式的文件。这一 .pyc 文件在你下一次从其它不同的程序导入模块时非常有用——它将更加快速，因为导入模块时所需要的一部分处理工作已经完成了。同时，这些按字节码编译的文件是独立于运行平台的。
### from..import 语句
如果你希望直接将 argv 变量导入你的程序（为了避免每次都要输入 sys. ），那么你可以通过使用 from sys import argv 语句来实现这一点。  
警告：一般来说，你应该尽量避免使用 from...import 语句，而去使用 import 语句。这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。  
```
from math import sqrt
print("Square root of 16 is", sqrt(16))
```
from mymodule import *  语句将导入诸如 say_hi 等所有公共名称，但不会导入 __version__ 名称，因为后者以双下划线开头
### 模块的 __name__
可用于确定模块是独立运行的还是被导入进来运行的。当模块第一次被导入时，它所包含的代码将被执行
```
if __name__ == '__main__':
print('This program is being run by itself')
else:
print('I am being imported from another module')
```
分别运行 python test.py 及 import test
### import this 语句打印出 The Zen of Python
### dir 函数
内置的 dir() 函数能够返回由对象所定义的名称列表。如果这一对象是一个模块，则该列表会包括函数内所定义的函数、类与变量。
如果没有提供参数，函数将返回当前模块的名称列表。
```
a = 5
dir() # Compares with below
del a
dir()

dir(str)  # 字符串的属性
```
同时，还有一个 vars() 函数也可以返回给你这些值的属性，但只是可能，它并不能针对所有类都能正常工作。
### 包
用以组织你的程序的层次结构
包是指一个包含模块与一个特殊的 __init__.py 文件的文件夹，后者向 Python 表明这一文 件夹是特别的，因为其包含了 Python 模块。
### 总结
如同函数是程序中的可重用部分那般，模块是一种可重用的程序。包是用以组织模块的另一种层次结构。Python 所附带的标准库就是这样一组有关包与模块的例子

## 数据结构
它们只是一种结构，能够将一些数据聚合在一起。换句话说，它们是用来存储一系列相关数据的集合。
Python 中有四种内置的数据结构——列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）。我们将了解如何使用它们，并利用它们将我们的编程之路变得更加简单。
### 列表
列表是一种用于保存一系列**有序项目**的集合，也就是说，你可以利用列表保存一串项目的序列。
一旦你创建了一张列表，你可以添加、移除或搜索列表中的项目。意即，可变的（Mutable）数据类型。*字符串是不可变的（Immutable)*
### 对象与类 []
列表是使用对象与类的实例。当我们启用一个变量 i 并将整数 5 赋值给它时，你可以认为 这是在创建一个 int 类（即类型）之下的对象（即实例）
一个类也可以带有方法（Method），也就是说对这个类定义仅对于它启用某个函数。
一个类同样也可以具有字段（Field），它是只为该类定义且只为该类所用的变量。
### 元组 ()
元组（Tuple）用于将多个对象保存到一起。元组的一大特征类似于字符串，它们是不可变的。
我们能够看到 len 函数在此处用来获取元组的长度。这也表明元组同时也是一个序列
### 字典
键值对, 类似 d = {key : value1 , key2 : value2} ; 字典中的键值对是无序的
只能使用不可变的对象（如字符串）作为字典的键值
判断 key 是否在字典 dict 中，可用 if 'key' in dict:
### 关键字参数与字典
如果你曾在你的函数中使用过关键词参数，那么你就已经使用过字典了！你只要这么想——你在定义函数时的参数列表时，就指定了相关的键值—值配对。当你在你的函数中访问某一变量时，它其实就是在访问字典中的某个键值。（在编译器设计的术语中，这叫作符号表（Symbol Table））
### 序列
列表、元组和字符串可以看作序列（Sequence）的某种表现形式
序列的主要功能是资格测试（Membership Test）（也就是 in 与 not in 表达式）和索引操作（Indexing Operations, 这也被称作下标操作（Subscription Operation）），它们能够允许我们直接获取序列中的特定项目
- 索引操作也可以使用负数，在这种情况下，位置计数将从队列的末尾开始。因此， shoplist[-1] 指的是序列的最后一个项目
序列还拥有一种切片（Slicing）运算符，它能够允许我们序列中的某段切片——也就是序列之中的一部分。
- 序列切片将包括起始位置，但不包括结束位置。
- shoplist[:] 返回的是整个序列
- 同样可以在切片操作中使用负数位置: shoplist[:-1] 强返回一组序列切片，其中不包括序列的最后一项项目
- 同样可以在切片操作中提供第三个参数，这一参数将被视为切片的步长（Step）（在默认情况下，步长大小为 1）. 步长为负数表示从末尾开始读取
```
name = 'swaroop'
print(name[0]) # s
print('characters 2 to end is', name[2:]) aroop
```
### 集合
集合（Set）是简单对象的无序集合（Collection）。当集合中的项目**存在与否**比起次序或其出现次数更加重要时，我们就会使用集合。
通过使用集合，你可以测试某些对象的资格或情况，检查它们是否是其它集合的子集，找到两个集合的交集，等等。
```
country = set(['brazil', 'russia', 'india'])
'india' in bri  # True
'usa' in bri  # False

countryCopy = country.copy()
countryCopy.add('china')
countryCopy.issuperset(bri)  # True

bri.remove('russia')
country & countryCopy 或者 country.intersection(countryCopy)  # {'brazil', 'india'}
```
### 引用
当你创建了一个对象并将其分配给某个变量时，变量只会查阅（Refer）某个对象，并且它也不会代表对象本身。也就是说，变量名只是指向你计算机内存中存储了相应对象的那一部分。这叫作将名称绑定（Binding）给那一个对象。
```
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # 两者是指向同一对象的不同名称
mylist = shoplist[:] # 通过生成一份完整的切片制作一份列表的副本, 两者指向对象不同
```
你要记住如果你希望创建一份诸如序列等复杂对象的副本（而非整数这种简单的对象（Object）），你必须使用切片操作来制作副本。如果你仅仅是将一个变量名赋予给另一个名
称，那么它们都将“查阅”同一个对象.
### 有关字符串的更多内容
在程序中使用的所有字符串都是 str 类下的对象
```
name = 'Swaroop'
name.startswith('Swa')
'a' in name
name.find('war') != -1 # 用于定位字符串中给定的子字符串的位置

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist)) # 联结操作 Brazil_*_Russia_*_India_*_China
```
更多查阅 help(str) 

## 解决问题

## 面向对象编程
在至今我们编写的所有程序中，我们曾围绕函数设计我们的程序，也就是那些能够处理数据 的代码块。这被称作面向过程（Procedure-oriented）的编程方式。还有另外一种组织起你的 程序的方式，它将数据与功能进行组合，并将其包装在被称作“对象”的东西内。在大多数情况 下，你可以使用过程式编程，但是当你需要编写一个大型程序或面对某一更适合此方法的问 题时，你可以考虑使用面向对象式的编程技术。
类与对象是面向对象编程的两个主要方面。一个类（Class）能够创建一种新的类型 （Type），其中对象（Object）就是类的实例（Instance）。
这不同于 C++ 与 Java（1.5 版之前），在它们那儿整数是原始内置类型。C# 与 Java 1.5   程序员会发现这与装箱与拆箱（Boxing and Unboxing）概念颇有相似之处
对象可以使用属于它的普通变量来存储数据。这种从属于对象或类的变量叫作字段 （Field）。对象还可以使用属于类的函数来实现某些功能，这种函数叫作类的方法 （Method）。字段与方法通称类的属性（Attribute）
### self
类方法与普通函数只有一种特定的区别——前者必须有一个额外的名字，这个名字必须添加 到参数列表的开头，但是你不用在你调用这个功能时为这个参数赋值，Python  会为它提供。 这种特定的变量引用的是对象本身，按照惯例，它被赋予 self 这一名称。
Python 中的 self 相当于 C++ 中的指针以及 Java 与 C# 中的 this 指针
原理: myobject.method(arg1, arg2) 时，Python 将会自动将其转换成 MyClass.method(myobject, arg1, arg2)
### 类
```
将以下代码保存为 demo.py
class Person:
    pass  #一个空的代码块
p = Person() 
print(p)
执行 $ python demo.py  输出如下
<__main__.Person instance at 0x10171f518>
```
结果告诉我们我们在 Person 类的 __main__ 模块中拥有了一个实例。
要注意到在本例中还会打印出计算机内存中存储你的对象的地址。案例中给出的地址会与你 在你的电脑上所能看见的地址不相同，因为 Python 会在它找到的任何空间来存储对象。
### 方法
```
class Person:
    def say_hi(self):
        print('hi')
p = Person()
p.say_hi()
# 上述两行等同于 Person().say_hi(), 注意其中类有括号, 相当于匿名创建了一个 Person 实例
```
### __init__方法
该方法会在类的对象被实例化（Instantiated）时立即运行。这一方法可以对任何你想 进行操作的目标对象进行初始化（Initialization）操作
### 类变量与对象变量
数据部分——也就是字段——只不过是绑定（Bound）到类与对象的命名空间（Namespace）的普通变量。这就代表着这些名称仅在这些类与对象所存在的上下文中有效。这就是它们被称作“命名空间”的原因。
字段（Filed）有两种类型——类变量与对象变量，它们根据究竟是类还是对象拥有这些变量来进行分类。
```
class Person:
    """表示一个带有名字的人。"""
    count = 0   
    def __init__(self,  name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1
    @classmethod                
    def how_many(cls):  
        """打印出当前的人口数量"""                            
        print("We have {:d} persons.".format(cls.population))
```
count 属于 Person 类，因此它是一个类变量; name 变量属于一个对象（通过使用 self 分配），因此它是一个对象变量
要注意当一个对象变量与一个类变量名称相同时，类变量将会被隐藏
Person.count 等同于 self.\__class__.count
how\_many 实际上是一个属于类而非属于对象的方法。这就意味着我们可以将它定义为一个 classmethod（类方法） 或是一个 staticmethod（静态方法），这取决于我们是否知道我们需不需要知道我们属于哪个类。由于我们已经引用了一个类变量，因此我们使用  classmethod（类方法）。
此处使用装饰器（Decorator）将 how\_many 方法标记为类方法。你可以将装饰器想象为调用一个包装器（Wrapper）函数的快捷方式，因此启用 @classmethod 装饰器等价于调用：how\_many = classmethod(how_many)
Person.__doc__ 访问类的文档字符串，对于方法的文档字符串，则可以使用 Person.how_many.__doc__
所有的类成员都是公开的, 并且 Python 中所有的方法都是虚拟的（Virtual）。但有一个例外：如果你使用数据成员并在其名字中使用双下划线作为前缀，形成诸如 __privatevar 这样的形式，Python 会使用名称调整（Namemangling）来使其有效地成为一个私有变量
### 继承
面向对象编程的一大优点是对代码的重用（Reuse），重用的一种实现方法就是通过继承 （Inheritance）机制。继承最好是想象成在类之间实现类型与子类型（Type and Subtype） 关系的工具
多态性（Polymorphism），在任何情况下，如果父类型希望，子类型都可以被替换，也就是说，子对象可以被看作父类的实例
父类会被称作基类（Base Class）或是超类（Superclass）。子类（Subclass）会被称作派生类（Derived Classes）
要想使用继承，在定义类时我们需要在类后面跟一个包含基类名称的元组。如果继承元组（Inheritance Tuple）中有超过一个类，这种情 况就会被称作多重继承（Multiple   Inheritance）
子类中定义了 __init__ 方法，Python 不会自动调用基类 SchoolMember 的构造函数，你必须自己显式地调用它。相反，如果我们没有在一个子类中定义一个 __init__ 方法，Python 将会自动调用基类的构造函数。这个在自定义方法上也适用

## 输入与输出
我们可以分别通过 input() 函数与 print 函数来实现这一需求。
对于输入，我们还可以使用 str （String，字符串）类的各种方法。例如，你可以使用 rjust 方法来获得一个右对齐到指定宽度的字符串。你可以查看 help(str) 来了解更多细节。
另一个常见的输入输出类型是处理文件。创建、读取与写入文件对于很多程序来说是必不可少的功能，而我们将在本章探讨这一方面。
### 用户输入内容
判断输入字符串回文，忽略标点、空格与大小写
```
import string

forbidden = ('!',' ', ',', '.', ':','"',';')

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    lowertext = text.lower()

    # lowertext = lowertext.replace(' ','')
    # for char in string.punctuation:
    #     lowertext = lowertext.replace(char, '')

    for char in forbidden:
        lowertext = lowertext.replace(char, '')

    print(lowertext)
    return lowertext == reverse(lowertext)

testText = input('Enter a string:')
if is_palindrome(testText):
    print('It\'s palindrome')
else:
    print('not')
```
### 文件
通过创建一个属于 file 类的对象并适当使用它的 read 、 readline 、 write 方法来打开或使用文件，并对它们进行读取或写入；最后调用 close 方法来告诉 Python 我们已经完成了对该文件的使用
使用内置的 open 函数并指定文件名以及我们所希望使用的打开模式来打开一个文件。打开模式可以是阅读模式（ 'r' ），写入模式（ 'w' ）和追加模式（ 'a' ）。我们还
可以选择是通过文本模式（ 't' ）还是二进制模式（ 'b' ）来读取、写入或追加文本。实际上还有其它更多的模式可用， help(open) 会给你有关它们的更多细节。在默认情况
下， open() 会将文件视作文本（text）文件，并以阅读（read）模式打开它。
```
# 如果是 2.7 的版本需要加上此句  from __future__ import print_function

poem = '''I
Love
You
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    # 每行（`line`）的末尾都自动含有换行符，因为它是从一个文件中进行读取的
    print(line, end='')
f.close()
```
### Pickle
Python 提供了一个叫作 Pickle 的标准模块，通过它你可以将任何纯 Python 对象存储到一个文件中，并在稍后将其取回。这叫作持久地（Persistently）存储对象。
```
import pickle

shoplistfile ='shoplist.data'
shoplist = ['apple', 'banana', 'orange']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)
```
要想将一个对象存储到一个文件中，我们首先需要通过 open 以写入（write）二进制（binary）模式打开文件，然后调用 pickle 模块的 dump 函数。这一过程被称作封装
（Pickling）。接着，我们通过 pickle 模块的 load 函数接收返回的对象。这个过程被称作拆封（Unpickling）。
### Unicode
如果你正在使用 Python 2，我们又希望能够读写其它非英语语言，我们需要使用 unicode 类型，它全都以字母 u 开头，例如 u"hello world" 。
type(u"hello world")  输出 <type 'unicode'>
当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，我们需要将我们的 Unicode 字符串转换至一个能够被发送和接收的格式，这个格式叫作“UTF-8”。我们可以在这一格式下进行读取与写入，只需使用一个简单的关键字参数到我们的标准 open 函数中：
```
# encoding=utf-8
import io
f = io.open('abc.txt', 'wt', encoding='utf-8')
f.write(u'qwe')
f.close()

text = io.open('abc.txt', encoding='utf-8').read()
print(text)
```
每当我们诸如上面那番使用 Unicode 字面量编写一款程序时，我们必须确保 Python 程序已经被告知我们使用的是 UTF-8，因此我们必须将 # encoding=utf-8 这一注释放置在我们程序的顶端. 使用 io.open 并提供了“编码（Encoding）”与“解码（Decoding）”参数来告诉 Python 我们正在使用 Unicode。

## 异常
from baby
### 抛出异常
你可以通过 raise 语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出（Thrown）异常的对象。
你能够引发的错误或异常必须是直接或间接从属于 Exception （异常） 类的派生类
```
# encoding=utf-8

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('input st:')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except ShortInputException as sie:
    print('input text length is {}, expected at least {}').format(sie.length, sie.atleast)
else:
    print('No exception was raised')
# 其他工作能在此处继续正常运行
print('Going on')
```

### 错误 
如果我们把 print 误拼成 Print，Python 会抛出（Raise）一个语法错误。
```
>>> Print("Hello World") 
Traceback (most recent call last):
 File "<stdin>", line 1, in <module> 
NameError: name 'Print' is not defined
```
你会注意到一个 NameError 错误被抛出，同时 Python 还会打印出检测到的错误发生的位置。这就是一个错误错误处理器（Error Handler） 为这个错误所做的事情

### 处理异常
```
try:
    text = input('Enter someting:')
except KeyboardInterrupt:
    print('You cancelled the operation')
except EOFError:
    print('EOF operation')
else:
    print('You input {}'.format(text))
```
我们将所有可能引发异常或错误的语句放在 try 代码块中，并将相应的错误或异常的处理器 （Handler）放在 except 子句或代码块中。 except 子句可以处理某种特定的错误或异常，或者是一个在括号中列出的错误或异常。如果没有提供错误或异常的名称，它将处理所有错误与异常。
如果没有任何错误或异常被处理，那么将调用    Python  默认处理器，它只会终端程序执行并打 印出错误信息。
你还可以拥有一个 else 子句与 try..except 代码块相关联。 else 子句将在没有发生异常的时候执行

### 抛出异常
你可以通过 raise 语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出（Thrown）异常的对象。
你能够引发的错误或异常必须是直接或间接从属于 Exception （异常） 类的派生类。

### Try...finally
在 print 之后使用了 sys.stout.flush() ，以便它能被立即打印到屏幕上

### with 语句
在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式。因此，还有一个 with 语句使得这一过程可以以一种干净的姿态得以完成
在幕后发生的事情是有一项 with 语句所使用的协议（Protocol）。它会获取由 open 语句返回的对象，在本案例中就是“thefile”。它总会在代码块开始之前调用      thefile.__enter__ 函数，并且总会在代码块执行完毕之后调用 thefile.__exit__  。 因此，我们在 finally 代码块中编写的代码应该格外留心 __exit__ 方法的自动操作。这能够帮助我们避免重复显式使用 try..finally 语句

## 标准库
### sys 模块
```
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True
```

### 日志模块
```
import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),  #使用这一特殊函数，而非仅仅将这几段字符串拼凑在一起的原因是这个函数会确保完整的位置路径符合当前操作系统的预期格式
    'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
    'test.log')

print('Logging to', logging_file)

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w'
)

logging.debug('Starting')
logging.info('Do something')
logging.warning('End')
```
更多标准模块使用说明参考
https://docs.python.org/3/library/index.html
https://pymotw.com/2/contents.html

## 更多
### 传递元组
使用元组从一个函数中返回两个不同的值
```
>>> def get_error_details():
...     return (2, 'details')
```
a, b = <some expression> 的用法会将表达式的结果解释为具有两个值的一个元组。意味着交换两个变量的最快方法是： a, b = b, a

### 特殊方法
诸如 __init__ 和 __del__ 等一些方法对于类来说有特殊意义。
特殊方法用来模拟内置类型的某些行为。举个例子，如果你希望为你的类使用 x[key] 索引操作（就像你在列表与元组中使用的那样），那么你所需要做的只不过是实现__getitem__() 方法，然后你的工作就完成了。如果你试图理解它，就想想 Python 就是对list 类这样做的！

其他内置方法：参考 https://docs.python.org/3/reference/datamodel.html#special-method-names
__init__(self, ...)
这一方法在新创建的对象被返回准备使用时被调用。
__del__(self)
这一方法在对象被删除之前调用（它的使用时机不可预测，所以避免使用它）
__str__(self)
当我们使用 print 函数时，或 str() 被使用时就会被调用。
__lt__(self, other)
当小于运算符（<）被使用时被调用。类似地，使用其它所有运算符（+、> 等等）时都会有特殊方法被调用。
__getitem__(self, key)
使用 x[key] 索引操作时会被调用。
__len__(self)
当针对序列对象使用内置 len() 函数时会被调用

### Lambda
lambda 语句可以创建一个新的函数对象。从本质上说， lambda 需要一个参数，后跟一个表达式作为函数体，这一表达式执行的值将作为这个新函数的返回值
points = [{'x': 2, 'y': 3},
{'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])  # 表示按每个元素的第 'y' 个来排序
print(points)

#### 列表推导
列表推导（List Comprehension）用于从一份现有的列表中得到一份新列表。想象一下，现在你已经有了一份数字列表，你想得到一个相应的列表，其中的数字在大于 2 的情况下将乘以 2。列表推导就是这类情况的理想选择。
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

### 在函数中接收元组与字典
有一种特殊方法，即分别使用 * 或 ** 作为元组或字典的前缀，来使它们作为一个参数为函数所接收。当函数需要一个可变数量的实参时，这将颇为有用
```
def powerlist(power, *arg):
    total = 0
    for i in arg:
        total += pow(i, power)
    return total

print(powerlist(2,3,4))
```

### assert 语句
assert 语句用以断言（Assert）某事是真的。例如说你非常确定你正在使用的列表中至少包含一个元素，并想确认这一点，如果其不是真的，就抛出一个错误， assert 语句就是这种情况下的理想选择。当语句断言失败时，将会抛出 AssertionError 。
```
list = ['a']
assert len(list) >= 1
list.pop()
assert len(list) == 1

Traceback (most recent call last):
  File "test.py", line 4, in <module>
    assert len(list) == 1
AssertionError
```
你应该明智地选用 assert 语句。在大多数情况下，它好过捕获异常，也好过定位问题或向用户显示错误信息然后退出。

### 装饰器
装饰器（Decorators）是应用包装函数的快捷方式。这有助于将某一功能与一些代码一遍又一遍地“包装”。举个例子，我为自己创建了一个 retry 装饰器，这样我可以将其运用到任何函数之中，如果在一次运行中抛出了任何错误，它就会尝试重新运行，直到最大次数 5 次，并且每次运行期间都会有一定的延迟。这对于你在对一台远程计算机进行网络调用的情况十分有用：
示例未实际操作一边