from time import sleep
def LToS(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def anagram():
    listA = []
    listB = []
    wordA = list(input("Type first word to compare: "))
    wordB = list(input("Type second word to compare: "))
    sleep(0.25)
    
    print("Decomposed and sorted first word:")
    sleep(0.3)
    for i in range(0,int(len(wordA))):
        listA.append(wordA[i])
    sortedA = sorted(listA)
    print(sortedA)
    sleep(0.3)
    print("Decomposed and sorted second word:")
    sleep(0.3)
    for i in range(0,int(len(wordB))):
        listB.append(wordB[i])
    sortedB = sorted(listB)
    print(sortedB)
    print("_________________________________")
    sleep(1)
    if sortedA == sortedB:
        print(LToS(wordA),"and",LToS(wordB),"are anagrams")
    else:
        print(LToS(wordA),"and",LToS(wordB),"aren't anagrams")
        

anagram()
