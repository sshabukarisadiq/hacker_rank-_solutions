n = int(input("enter a positive number : "))
if n%2 == 1:
    print("wired")
elif n % 2 == 0 and 2 <= n <= 5 :
    print("not wired")
elif n % 2 == 0 and 6 <= n <= 20:
    print("wired")
elif n % 2 ==0 and n>=20:
    print ("not wired")