#!/usr/bin/python
def karatsuba(x,y,n):
    if n == 1:
        return x*y
    n1 = n/2
    n2 = n-n1
    a = x/pow(10,n2)
    c = y/pow(10,n2)
    b = x-a*pow(10,n2)
    d = y-c*pow(10,n2)
    ac = karatsuba(a,c,n1)
    bd = karatsuba(b,d,n2)
    #aplusb = a*pow(10,n1)+b
    #cplusd = c*pow(10,n1)+d
    aplusb = a+b
    cplusd = c+d
    return ac*pow(10,n)+(aplusb*cplusd - ac - bd)*pow(10,n1)+bd

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627,64))
    
