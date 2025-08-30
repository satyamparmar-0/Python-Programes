n=7
for i in range(11):
    print(i*n)

# multiplication table in python

# for specific word we use startwith()
lst=["atyam","chanki","rahul"]
for i in lst:
    if i.startswith("s"):
        print("hello "+i)

# given number is prime or not
i=int(input("enter any number "))
prime=True
for n in range(2,i):
    if n%i==0:
        prime=False
        break
if prime:
    print("the number is prime ")
else:
    print("the number is not prime")

# while loop
i = 0
while i < 5:
    print("Iteration:", i)
    i += 1

# do while loop
i = 0
while True:
    print("Iteration:", i)
    i += 1
    if i >= 5:
        break

