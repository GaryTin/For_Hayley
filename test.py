a = "apple"
input = "abecd"

i= 0
for word in input:
    if word in a :
        if a[i] == word:
            print("Green")
        else:
            print("Yellow")
    else:
        print("Grey")
    i+=1

print("testing")
