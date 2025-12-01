seq= []

print ("Enter the number of elements in the sequence:")
n = int(input())
print ("Enter the elements of the sequence:")

for i in range(0, n):
    element = int(input())
    seq.append(element)

for i in range (n-1) :
    if seq[i] == seq[i+1] :
        print("true")
        break
    else :
        print("false")
        break

