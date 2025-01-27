print(0)
print(1)
count = 2
def fibonacci(num1, num2):
    global count
    if count <= 19:
        new_fibo = num1 + num2
        print(new_fibo)
        num1 = num2
        num2 = new_fibo
        count +=1
        fibonacci(num1, num2)
    else:
        return

fibonacci(0 ,1)
