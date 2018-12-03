


# 阶乘
def factorial(n) :
  if n == 1 :
    return 1         #递归结束
  return n * factorial(n - 1)  #问题规模减1，递归调用

# 汉诺塔
i = 1
def move(n, mfrom, mto) :
    global i
    print ("第%d步:将%d号盘子从%s -> %s" %(i, n, mfrom, mto))
    i += 1

def Hanoi(n, A, B, C):
    if n == 1 :
        move(1,A, C )
    else:
        Hanoi(n-1, A,C,B)
        move(n,A,C)
        Hanoi(n-1, B,A,C)

try :
      n = int(5)
      print ("移动步骤如下：")
      Hanoi(n, 'A', 'B', 'C')
except ValueError:
      print ("please input a integer n(n > 0)!)")


# 斐波那契数列问题
# 从第三项起，每一项都等于前两项的和，即F(N) = F(N - 1) + F(N - 2) (N >= 2)
# 并且规定F(0) = 0，F(1) = 1
def  Fibonacci(n):
    if n == 1 : return 1
    if n == 2 : return 1
    return Fibonacci(n-1) + Fibonacci(n-2)
print('请输入需要打印的斐波那契数列项数n的值：')


list_F = [0]
count = 1

try:
    n = int(input('enter:'))  #input()接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型
except:
    print('请输入一个整数')
    exit()

while(count <= n):
    list_F.append(Fibonacci(count))
    count +=1
print(list_F)


# 欧几里得算法（辗转相除法）
def Euclidean_algorithm(a,b):
    m = b % a
    if m == 0: return a
    return Euclidean_algorithm(m,a)

a = 20
b = 3
print(Euclidean_algorithm(a,b))