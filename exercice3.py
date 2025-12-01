Fibonacci=[]
for i in range (0,50):
    if i == 0:
        Fibonacci.append(0)
    elif i == 1:
        Fibonacci.append(1)
    elif Fibonacci[i-1] + Fibonacci[i-2] < 50:
        Fibonacci.append(Fibonacci[i-1] + Fibonacci[i-2])
    else:
        break
    print(Fibonacci[i])
