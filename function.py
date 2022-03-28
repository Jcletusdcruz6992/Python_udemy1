def my_fun(par='default'):
    print( 'My first python, function {a} '.format(a=par))
my_fun()

def hello():
    return 'hello'
result=hello()
print(result)

def add_num(num1,num2):
    if(type(num1)==type(num2)==type(10)):
        return(num1+num2)
    else:
        return 'Plase enter integer inputs'
res=add_num(16,3)
print(res)


my_list=[1,2,3,4,5,6,7,8,9,10]

def even(num):
    return num%2==0
nums=filter(even,my_list)
print(list(nums))
nume=filter(lambda numer:numer%2==0,my_list)
print(list(nume))


tweet='Go Sports, #sports'
res=tweet.split('#')[1]
print(res)

print('x' in [1,2,3])
print('x' in [1,2,3,'x'])
