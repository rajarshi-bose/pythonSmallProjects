def palindrome(word):
    x = 0
    for i in range(0,int(len(word)/2)):
        if word[i] != word[(len(word)-i)-1]:
            print("letter",i + 1,"didn't match")
            break
        else:
            print("letter",i + 1,"matched")
            x = x + 1

    if x == int(len(word)/2):
        print("is palindrome")
    else:
        print("is not palindrome")
            
palindrome("stuntnuts")
