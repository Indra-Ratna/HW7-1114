#Indra Ratna
#CS-UY 1114
#1 Nov 2018
#Homework 7

#Problem 2
def avg(numbers):
    acc = 0
    count = 0
    for value in numbers:
        if value != []:
            count+=1
            acc += value
    if count > 0:
        mean = acc/count
        return mean

#Problem 3
def sum_some(lower, upper, numbers):
    acc = 0
    count = 0
    for number in numbers:
        if( number <= upper and number >= lower):
            acc+=number
            count+=1
    if(count>0):
        return acc
    return 0

#Problem 4
def is_sorted(numbers):
    if len(numbers)>1:
        for index in range (len(numbers)-1):
            if(numbers[index]>numbers[index+1]):
                return False
    return True

#Problem 5
def indices (needle,haystack):
    acc = []
    index =0
    while index < len(haystack):
        if (haystack[index] == needle):
            acc.append(index)
        index+=1
    return acc

#Problem 6
def intersperse():
    s1 = input("Enter a sentence: ")
    s2 = input("Enter a sentence: ")
    s1 =s1.split()
    s2 =s2.split()
    acc = ""
    if (len(s1)>len(s2)):
        for index in range (len(s2)):
            acc += str(s1[index])+"  "+str(s2[index])+" "
        for index in range (len(s2), len(s1)):
            acc+=str(s1[index])+ " "
    elif(len(s1)==len(s2)):
        for index in range(len(s1)):
            acc+=str(s1[index])+" "+str(s2[index])+" "
    else:
        for index in range (len(s1)):
            acc+= str(s1[index])+" "+str(s2[index])+" "
        for index in range (len(s1), len(s2)):
            acc+=str(s2[index])+" "
    print (acc)

#Problem 7
def rlencode(s):
    final = []
    count = 0
    temp = 0
    index = 0
    while index < len(s):
        for letter in (s):
            if(s[index]==letter):
                count+=1
            else:
                index+=1
        final.append((letter,count))
    return final
def rldecode(rle):
    acc = ""
    for(letter, count) in rle:
        acc+=(letter*count)
    return acc

#Problem 8
def reverse_mut(xs):
    list = xs.copy()
    for element in list:
        xs.insert(0,element)
    for element in list:
        xs.pop(len(list)-1)
    return xs

def reverse_pure(xs):
    xs = xs[::-1]
    return(xs)

def test():
    print(avg([1,2,3,4,5,6]))
    print(avg([1,2,[],3,[],4]))
    print(sum_some(1,5,[1,2,3,4,5,6]))
    print(is_sorted([3,2,1]))
    print(is_sorted([1]))
    print(indices(7,[0,7,1,7,2,7,3]))
    intersperse("This is a test","of the emergency broadcast system.")
    intersperse("It is an ancient mariner","Who stoppeth one of three")
    intersperse("Five","for the symbols at your door")
    myList = [5,12,13,14,15]
    print(reverse_mut(myList))
    print(myList)
    print(reverse_pure(myList))
test()
