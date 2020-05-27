responses = ['Welcome to smart calculator', 'My name is Johny', 'Thanks', 'Sorry, this is beyond my ability, may be you could seperate your multi string with minus sign -']



def extract_numbers_from_text(text):
    l = []
    for t in text.split(' '):  # as we know the result of split function is a list of strings.
        try:
            l.append(float(t))
        except ValueError:
            pass
    return (l)



def lcm(a,b):
    L = a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1



def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1



def add(a,b):
    return a+b



def sub(a,b):
    return a-b



def multiply(a,b):
    return a*b



def division(a,b):
    return a/b



def end():
    print(responses[2])
    input('Press enter key to exit')
    exit()



def myname():
    print(responses[1])



def sorry():
    print(responses[3])



# volume of a cuboid is length*breadth*height
def vol_cuboid(l,b,h):
    #l, b, h = [eval(i) for i in input('enter length, breadth and height of cuboid').split()]
    # print('required area of cuboid is\n')
    #  we have implemented in sych a way that we have to provide some inputs, we can not write like this or can not leave parameters as blank. we can not take inputs here as we have written in above two line.
    return (l*b*h)



def area_triangle(b,h):
    return 1/2*b*h



def area_circle(radius):
    return 3.14*radius*radius



# simple interest formula = (principle_amount * rate_of_interest * time_duration)/100
def simple_interest(p,r,t):
    #p,r,t = [eval(i) for i in input('enter principle amount, rate of interest and time duration').split()]
    #print('requires simple interest = ',(p*r*t)/100)
    return (p*r*t)/100



def square_of_num(n):
    return n*n



def cube_of_num(n):
    return n*n*n



# checking even odd
def even_odd(x):
    if x%2==0:
        return '%d is even'%x
    else:
        return '%d is odd' %x



''' check weather a given number is positive negative or zero '''
def positive_negative_zero(n):
    if n == 0:
        return 'number is 0'
    elif n < 0:
        return '%d is negative'%n
    else:
        return '%d is positive'%n



''' greater among three numbers'''
def greater_among_three_num(x,y,z):
    if x>y:
        if x>z:
            return "greater is %d"%x
        elif x<z:
            return "greater is %d"%z
    elif y>z:
        return "greater is %d"%y
    else:
        return "greater is %d"%z



''' checking whether year is leap or not '''
def leap_year(yr):
    if yr%4==0:
        return "year %d is leap"%yr
    else:
        return "year %d is not leap"%yr



''' printing first N natural numbers '''
def first_N_natural_num(n):
    x = 1
    list_of_first_N_natural_numbers = []
    while x<=n:
        list_of_first_N_natural_numbers.append(x)
        x += 1
    print('list of first %d natural numbers is\n'%n)
    return list_of_first_N_natural_numbers




# first N natural numbers in reverse order are
def first_N_natural_num_reverse_order(n):
    x = n
    list_of_first_N_natural_numbers_reverse_order = []
    while n>=1:
        list_of_first_N_natural_numbers_reverse_order.append(n)
        n-=1
    print('first %d natural numbers in reverse order are' %x)
    return list_of_first_N_natural_numbers_reverse_order




''' python script to check weather a given number is prime or not '''
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 'not prime'
    else:
        return 'prime'




''' python script to print next prime number of a given number '''
def next_prime(n):
    y = n + 1
    for i in range(2, y):
        if y % i == 0:
            y = y + 1
    else:
        return 'next prime number after %d is' % n, y





''' python script to print first N prime numbers '''
def first_N_prime_num(n):
    count = 1
    y = 1
    li = []
    print('first %d prime numbers are'%n)
    while count<=n:
        for i in range(2,y):
            if y%i==0:
                y = y+1
        else:
            count = count+1
        li.append(y)
        y = y+1
    return li




''' python script to print all prime numbers between two given numbers '''
def prime_bw_two_numbers(n,m):
    li = []
    print('list of prime numbers range between %d and %d are'%(n,m))
    for i in range(n,m+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            li.append(i)
    return li



''' python script to calculating digits of a given number '''
def counting_digits(x):
    y = x
    count = 0
    while x!=0:
        x = x//10
        count = count + 1
    return 'no of digits in %d are'%y,count




''' python script for calculating sum of digits of a given number '''
def sum_digits(x):
    y = x
    sum = 0
    while x!=0:
        remainder = x%10
        #print(remainder,sep=',')
        sum = sum + remainder
        x = x//10
    return 'required sum of digits of %d is'%y,sum




''' python script to reverse the digits of a number '''
def reverse_the_digits(x):
    z = x
    reverse = 0
    while x!=0:
        remainder = x%10
        reverse = reverse*10+remainder
        x = x//10
    return 'reverse of %d is'%z,reverse,'  please ignore .0'




# checking whether a number is armstrong or not
def checking_armstrong(x):
    y = x
    sum = 0
    while x != 0:
        remainder = x % 10
        sum = sum + remainder ** len(str(y))
        x = x // 10
    # print(sum)
    if sum == y:
        return '%d is an armstrong number' % y
    else:
        return '%d is not an armstrong number' % y




# finding all armstrong numbers b/w two given numbers
def armstrong_bw_two_num(smaller, larger):
    lis = []
    for x in range(smaller, larger):
        b = x
        a = 0
        while x != 0:
            y = x % 10
            w = y ** len(str(b))
            a = a + w
            x = x // 10
            # w = 0        # w = 0 likho ya na likho, koi prob nahi

        if a == b:
            lis.append(a)
    return lis



# operations2 wali dictionary me 2 inputs liye jaayenge.
operations2 = {"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUBTRACTION":sub,"SUBTRACT":sub,"DIFFERENCE":sub,"PRODUCT":multiply,"MULTIPLICATION":multiply,"MULTIPLY":multiply,"DIVIDE":division,"DIVISION":division,"LCM":lcm,"MULTIPLE":lcm,"HCF":hcf,"FACTOR":hcf,"GREATEST-COMMON-DIVISOR":hcf,"GCD":hcf,"TRIANGLE":area_triangle,"BETWEEN":prime_bw_two_numbers,"RANGE":prime_bw_two_numbers,"ARMSTRONG":armstrong_bw_two_num}



# operations1 wali dictionary me 1 input liya jaayega.
operations1 = {"CIRCLE":area_circle,"SQUARE":square_of_num,"CUBE":cube_of_num,"EVEN":even_odd,"ODD":even_odd,"POSITIVE":positive_negative_zero,"NEGATIVE":positive_negative_zero,"ZERO":positive_negative_zero,"LEAP":leap_year,"NATURAL":first_N_natural_num,"REVERSE-ORDER":first_N_natural_num_reverse_order,"PRIME":prime,"NEXT-PRIME":next_prime,"PRIME-NUMBERS":first_N_prime_num,"DIGITS":counting_digits,"SUM-OF-DIGITS":sum_digits,"REVERSE":reverse_the_digits,"ARMSTRONG":checking_armstrong}



# operations3 wali dictionary me 3 inputs liye jaayenge.
operations3 = {"CUBOID":vol_cuboid,"INTEREST":simple_interest,"GREATEST":greater_among_three_num,"GREATER":greater_among_three_num,"THREE":greater_among_three_num}



commands = {"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"QUIT":end}