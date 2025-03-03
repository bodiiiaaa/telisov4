a=[0,1,0,12,3]

a=[b for b in a if b !=0] + [0] * a.count(0)

print(a)