k=eval(input ("input a number:"))
prime_number=[]
prime_number.append(2)
for a in range(2,k+1):
    c=0
    for b in prime_number:
        if a%b==0:
            c=1
            break
    if c==0:
        prime_number.append(a)
print(len(prime_number))
print(prime_number)
