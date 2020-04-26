missing=0
a=0
b=0
c=0
d=0

print("""

This program solves the common math problem where you have 2 equivalent fractions with one of the numbers missing in the form of (a/b)=(c/d), in that order. 

This might illustrate it better: 


 a           c
---    =    ---
 b           d


But you know 3 of the 4 variables and are trying to figure out the one you don't know. 

""")

while str(missing) not in ("a" "b" "c" "d"):
    missing = input("Which is missing? a or b or c or d? : ")
    
if missing=="a":
    print("a is being solved for")
    b=float(input("enter b: "))
    c=float(input("enter c: "))
    d=float(input("enter d: "))
    print()
    f=((c/d)*b)
    g=((b/d)*c)
    h=((b*c)/d)
    if (f==g and f==h and g==h and ((f/b)==(c/d)))==True:
        print("\n"+"the methods seem to agree that a is "+str(f)+" and (a/b)=(c/d)")
    elif (f==g and f==h and g==h and ((f/b)==(c/d)))==False:
        print("hmm. The methods don't agree and/or the check that (a/b)=(c/d) has failed when the result from method 1 is set as a. This shouldn't happen. Please report this problem and what was inputed to cause this.")
        print("method 1 of 3 says a is "+str(f))
        print("method 2 of 3 says a is "+str(g))
        print("method 3 of 3 says a is "+str(h))
        if ((f/b)==(c/d))==True:
            print("((a/b)=(c/d)) is True")
        elif ((f/b)==(c/d))==False:
            print("((a/b)=(c/d)) is False when "+str(f)+" from method 1 is set as a")

if missing=="b":
    a=float(input("enter a: "))
    print("b is being solved for")
    c=float(input("enter c: "))
    d=float(input("enter d: "))
    print()
    e=((a/c)*d)
    g=((d/c)*a)
    h=((a*d)/c)
    if (e==g and e==h and g==h and ((a/e)==(c/d)))==True:
        print("\n"+"the methods seem to agree that b is "+str(e)+" and (a/b)=(c/d)")
    elif (e==g and e==h and g==h and ((a/e==(c/d))))==False:
        print("hmm. The methods don't agree and/or the check that (a/b)=(c/d) has failed when the result from method 1 is set as b. This shouldn't happen. Please report this problem and what was inputed to cause this.")
        print("method 1 of 3 says b is "+str(e))
        print("method 2 of 3 says b is "+str(g))
        print("method 3 of 3 says b is "+str(h))
        if ((a/e)==(c/d))==True:
            print("((a/b)==(c/d)) is True")
        elif ((a/e)==(c/d))==False:
            print("((a/b)=(c/d)) is False when "+str(e)+" from method 1 is set as b")

if missing=="c":
    a=float(input("enter a: "))
    b=float(input("enter b: "))
    print("c is being solved for")
    d=float(input("enter d: "))
    print()
    e=((a/b)*d)
    f=((d/b)*a)
    h=((a*d)/b)
    if (e==f and e==h and f==h and ((a/b)==(e/d)))==True:
        print("\n"+"the methods seem to agree that c is "+str(e)+" and (a/b)=(c/d)")
    elif (e==f and e==h and f==h and ((a/b==(e/d))))==False:
        print("hmm. The methods don't agree and/or the check that (a/b)=(c/d) has failed when the result from method 1 is set as c. This shouldn't happen. Please report this problem and what was inputed to cause this.")
        print("method 1 of 3 says c is "+str(e))
        print("method 1 of 3 says c is "+str(f))
        print("method 1 of 3 says c is "+str(h))
        if ((a/b)==(e/d))==True:
            print("((a/b)==(c/d)) is True")
        elif ((a/b)==(e/d))==False:
            print("((a/b)=(c/d)) is False when "+str(e)+" from method 1 is set as c")

if missing=="d":
    a=float(input("enter a: "))
    b=float(input("enter b: "))
    c=float(input("enter c: "))
    print("d is being solved for")
    print()
    e=((b/a)*c)
    f=((c/a)*b)
    g=((c*b)/a)
    if (e==f and e==g and f==g and ((a/b)==(c/e)))==True:
        print("\n"+"the methods seem to agree that d is "+str(e)+" and (a/b)=(c/d)")
    elif (e==f and e==g and f==g and ((a/b)==(c/e)))==False:
        print("hmm. The methods don't agree and/or the check that (a/b)=(c/d) has failed when the result from method 1 is set as d. This shouldn't happen. Please report this problem and what was inputed to cause this.")
        print("method 1 of 3 says d is "+str(e))
        print("method 1 of 3 says d is "+str(f))
        print("method 1 of 3 says d is "+str(g))
        if ((a/b)==(c/e))==True:
            print("((a/b)==(c/d)) is True")
        elif ((a/b)==(c/e))==False:
            print("((a/b)=(c/d)) is False when "+str(e)+" from method 1 is set as d")
