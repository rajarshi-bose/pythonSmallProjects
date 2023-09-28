from time import sleep
from math import *
whichPrime = int(input("Which prime number do you want to find: "))

primeList = [2]
for i in range (3,10 * whichPrime): #moves to next number
    count = 0
    for item in range(0,len(primeList)): #checks with all primes in primeList
        primeCheck = i % primeList[item]
        if primeCheck == 0:
            print(i,"/",primeList[item],"=",i/primeList[item])
            print(i,"is composite, SKIPPED")
            break
        elif primeCheck != 0:
            sleep(0.025)
            print(i % primeList[item],",number = ",i,", divisor = ",primeList[item])
            count = count + 1
    #print("count",count)
    if count == len(primeList):
        print(count, "=", len(primeList),", PRIME",i,"ADDED")
        primeList.append(i)
    elif len(primeList) == whichPrime:
        break
    print("___________________________")
    
suffix = ''
lastNum = list(str(whichPrime))
if lastNum[-1] == '2':
    suffix = 'nd'
elif lastNum[-1] == '1':
    suffix = 'st'
elif lastNum[-1] == '3':
    suffix = 'rd'
else:
    suffix = 'th'

print("_________________________\n")
print(str(whichPrime) + suffix,"prime number is",primeList[whichPrime - 1])