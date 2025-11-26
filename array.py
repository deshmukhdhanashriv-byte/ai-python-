#updating a value

Myfruits=['banana','mango','apple','orange']
Myfruits[0]='kiwi'
print(Myfruits)

#inserting a array value

myfruits = ['banana', 'mango']
myfruits.insert(1, 'kiwi')
print(myfruits)

#inserting using append

myfruits=['banana','mango']
myfruits.append('apple')
print(myfruits)

#removing an array value

myfruits =['banana', 'mango', 'apple', 'orange']
myfruits.remove('mango')
print(myfruits)

#removing using pop

myfruits =['banana', 'mango', 'apple', 'orange']
myfruits.pop(2)
print(myfruits)

#finding length of an array

myfruits = ['banana', 'mango', 'apple', 'orange']
print(len(myfruits))

#lopping in array

myfruits = ['banana', 'mango', 'apple', 'orange']
for fruit in myfruits:
    print(fruit)

#looping in an array using index

myfruits = ['banana', 'mango', 'apple', 'orange']
for i in range(len(myfruits)):
    print( myfruits[i])

