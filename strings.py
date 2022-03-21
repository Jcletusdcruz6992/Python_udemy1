my_string="abcde"
print(my_string)
print(my_string[0])
print(my_string[-1])
print(my_string[4])
print(my_string[2:])
print(my_string[:2])
print(my_string[1:4])
print(my_string[:])
print(my_string[::])
print(my_string[::])
print(my_string[::2])
print(my_string[::3])

x=my_string.upper()
print(x)
x=x.lower()
print(x)
x=x.capitalize()
print(x)

string_two="Hello World"
x=string_two.split()
print(x)


x=string_two.split('o')
print(x)

x='item One:{} and item two:{}'.format('dog','cat')
print(x)

x='item One:{b} and item two:{a}'.format(a='dog',b='cat')
print(x)
