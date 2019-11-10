# coding=utf-8

# hello world
print("Hello World!")

# 井号后边的叫 注释，主要用于帮助理解代码，机器不会执行哦！
# 下面是 if..else 用法
if(1 == 2): 			# == 是用于计算其左右两边的值是否相等， 相等就是 True 不想等就是 False, True/False 是 ‘布尔’ 类型数据，表示真/假。if elif 后边的括号里最终是 True或False, 才能指导if 语句是否执行里边的程序
    print("1 == 2")		# 1 肯定不等于2， 所以这句不会执行哦
elif (1 == 3):			# elif 可以有多个哦
	print("1 == 3")		# 同样不会执行
else:
	print("else")		# 以上所有if ,elif 都不满足条件，那就是其他啦，这句会执行




# 2019.10.25 variate(变量)
# 变量是编程通用叫法，顾名思义，就是可以改变的量，类似于小学数学公式： y = ax + b， a和b是常量，保持不变，x可以取任意实数，就是变量
# 程序中的变量不仅可以是数字，也可以是一句话，一串数字或单词等，
# 每个变量都有个名字，在编程是就是这个变量的身份证，所以不要重名哦

print("\n*** 2019.10.25 variate-part1 ***") 
# print 的引号内几乎可以放进任何字符（字符可以认为是汉字、字母，甚至空格等），我们就用这种漂亮的title作为每天的间隔吧！
# 其中的\n表示换行，所以计算机里的换行也是一个字符哦， \ 是一种特殊用法，以后会讲哦

# 整数变量，也可以叫 int 型变量，取自英文 Integer
int_var = 10 # '=' 是赋值操作，将右边的值赋给左边的变量。 作业：【自行学习python变量的命名规范， 可以添加到注释中哦，以便以后复习】
#变量命名规范：1.只能用字母，数字，下划线；2.不能用数字开头，因为数字是常量。3.规范吧，单词之间用下划线连接。
result = int_var * 10 # 把变量 int_var 乘以 10 结果赋值给新的变量 result，只要程序不退出，这个变量值会一直被记得哦
print(result)
int_var = 200 # 变量嘛，可以随意修改它的值，就是把一个新的值甚至一个新的变量赋值给它就行了
int_var2 = 300
print(int_var)
int_var = int_var2
print(int_var)
                # 空行可以任意添加哈，不影响程序，一般用法是为了区分两部分代码，使得代码可读性好。
# 小数变量， 也可以叫float 型变量，取自英文 Float,字面意思浮动，计算机里代表小数点的位置变化代表了小数的变化
float_var = 10.1 # 把小数赋值给变量，其实python里你赋值给变量是什么类型，变量就自动会是什么类型，同样可以 float_var = 10, 这样就是整数变量了，只不过跟变量的字面意思不一致了，所以要好好取变量名哦，最好一看就知道变量里存的什么
print(float_var)
# 布尔变量， 也可以叫 boolean 型变量， 是一种 只能表示两种值的变量，它的值只有 True 和 False
boolean_True = True # 等号右边这个东西就是一个True值，写法强制要求，False同理
boolean_False = False
# 字符串变量，也可以叫 str 变量，取自英文String
str_var = "Hello World!" # 引号引起来的就是一个字符串，把它赋值给了str_var




# 2019.10.26 variate - part2(变量2)
# 上一节学的有点多，那就来做个小游戏吧
# 这个小游戏通过一个人身高和是否有胡须，来判断他/她是男生还是女生
print("\n*** 2019.10.26 variate-part2 ***")
stature = 180       # 身高，可以是小数，也可以是整数，python 中这两种类型变量之间是可以做运算的
is_beard = True    # 是否有胡须

reason = ""         # 判断理由，是一句话, 最开始赋值一个空的
sex_result = ""     # 判断结果，用 "man", "woman" 记录男女

if is_beard: # 其实if elif 都是通过判断其后边是个True还是False 来决定是否执行本部分的
    reason = "you have beard, "
    sex_result = "man"
elif stature >= 175: # >= 是一种比较运算，如果左边大于等于右边，就告诉elif 满足条件，就会执行这一块代码
    reason = "but you are tall, "
    sex_result = "man"
else:
    reason = "you do not have beard and you are dapper, "
    sex_result = "woman"

print("sex judging result:")
print(reason + "so you may be a")
print(sex_result)    
# 改变 stature 和 is_beard 的值，看看程序能不能分辨男女吧


# 2019.11.3 variate - part3(变量3)
# 上两节已经学习了 整数、小数（浮点数）、布尔、字符串 类型的变量，这些都是最基本的python变量类型
# 本节继续学习变量类型，在基本变量类型之上还有哪些常用类型
print("\n*** 2019.11.3 variate-part3 ***")

# 列表变量，也叫 list 变量， 也叫数组（虽然字面上是数组，实际上是各种类型都可以的组）
empty_list = [] # 最简单的列表，中括号表示列表，中间没有任何东西，空的列表
name_list = ["XYY", "YDH"] # 列表中的每一项叫做“元素”， 可以是任意类型的数据，元素之间用逗号隔开， 注意逗号之后最好有个空格（规范）；这里有个名字的列表，有两个元素，都是字符串类型的
is_man = False
other_list = [100, 100.0, 'Hello World!', is_man] # 列表中的元素可以同时存在多种类型
nest_list = [[1, 2, 3], [4, 5, 6]] # 瞧瞧，列表的元素还可以是列表，这就是嵌套列表；这里嵌套了两层列表，叫做二维数组， 或 二维列表

print(empty_list)
print(name_list)
print(other_list)
print(nest_list)

# 很容易的，想用列表中的某个元素只需要知道这个元素的顺序
order_list = [1, 2, 3, 4, 5]
print(order_list[2]) # 列表变量后跟[x] 表示列表中第 x + 1 个元素，这也表明了列表中的元素是有顺序的， 也可以通过这种方式改变某个元素的值
order_list[2] = 100 # 修改第三个元素为 100
print(order_list)

# 字典变量，也叫 dict变量
# 字典是一种 key - value 格式的变量，key在字典中是不能重复的
empty_dict = {} # 字典用大括号表示，这是一个空字典
id_name_dict = {2: "XYY", 1: "YDH"} # 字典跟列表一样是由元素组成的，元素格式是 xxx: yyy, xxx 就是key, 基本python类型都可以作为key， yyy就是key对应的值， value不限制类型
print(empty_dict)
print(id_name_dict) # 输出会发现元素之间的顺序跟写的不一致，这也表明了字典中的元素是无序的，只能按 key 取值
print(id_name_dict[1]) # 取某一个key对应的value， 格式跟列表一样，中括号内写 key， 同样方式可以更改value值
id_name_dict[1] = "Dylan"
print(id_name_dict)

## 拓展思考
#1. 计算机中的数据库要求最基本的 增、删、改、查， 列表 和字典挺像一个微型的数据库， 它们也支持这些操作，去 google一下看看这些操作该怎么做吧～
#2. 字典中的key是唯一的，也就是不会有完全相同的两个key，在实际应用中有什么意义呢？想象作者当初为什么这么设计








