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
