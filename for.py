seq=[1,3,7,9,11]
for j in seq:
    print(j)
for j in seq:
    print('hello')
d={'Sam':1,'John':2,'Dcruz':3}
for i in d:
    print(i)
    print(d[i])
my_pairs=[(1,2),(3,4),(5,6)]
for i in my_pairs:
    print(i)
for (tup1,tup2) in my_pairs:

    print(tup2)
    print(tup1)
i=0
while i<5:
    print('i is: {}'.format(i))
    i=i+1


x=[1,2,3,4,5]
out=[]
for i in x:
    out.append(i**2)
print(out)
res=[num**2 for num in x]
print(res)
