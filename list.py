my_list=[1,2,4]
print(my_list)
list_two=['jam',1,2,4,[3,5,7],3.9]
print(list_two)
print(len(list_two))
list_three=['j','a','m']
print(list_three[0])
print(list_three[-1])
list_three[0]='answer'
print(list_three)
list_three.append("New Item")
print(list_three)
list_three.extend(['c','l','e'])
print(list_three)
print(list_three.pop(0))
print(list_three.pop())
print(list_three)
list_four=['a','b','c','d']
print(list_four.reverse())
a=my_list.sort()
print(a)
lis=[1,2,['s','e','b']]
print(lis[2])
print(lis[2][0])
matrix=[[1,2,3],[4,5,6],[7,8,9]]
var=[row[0] for row in matrix]
print(var)
