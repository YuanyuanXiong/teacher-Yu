# encoding=utf-8

if(1 == 2):
    print("i am")
elif(1 == 3):
    print("you are")
else:
    print("they are")
    
print("***\n***")
int_var = 250
int_var = int_var / 25
print(int_var)
int_var = int_var * 30
print(int_var)
float_var = 0.25
float_var = int_var * float_var
float_var = int_var * float_var
print(float_var)
str_var = "xiong"
print(str_var)

print("\n practice 20191030")
length = 10.1
width = 20.2
ratio = length / width 

if ratio > 1:
    print("length is longer，and the ratio is")
    print(ratio)
elif ratio == 1:
    print("this cell is square, and the ratio is")
    print(ratio)
else:
    print("width is longer,and the ratio is")
    print(ratio)