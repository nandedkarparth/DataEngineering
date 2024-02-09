from functools import reduce
li = [1,1,1,1,1,1,1,1,1,1,1,1]
sum = reduce((lambda x, y: x + y), li)
print(sum)