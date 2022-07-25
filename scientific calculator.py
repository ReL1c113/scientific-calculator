#SCIENTIFIC CALCULATOR
import math
while(True):
    print("CHOOSE WHAT OPERATION YOU WOULD LIKE TO PERFORM\n 1. ADDITION  2. MULTIPLICATION 3.DIVISION 4. SUBTRACTION\n 5. TRIGNOMETRIC VALUES OF DEGREE  6. CONVERT RADIANS IN DEGREE \n 7. SQUARE ROOT  8. CUBE  9. SQUARE\n 10. logₐ x  11. nCr(COMBINATION) 12. nPr(PERMUTATION) 13. FACTORIAL\n 14. x^y ")
    i=int(input())
    if i==1:
        print("\n HOW MANY NO. WOULD YOU LIKE TO ADD")
        j=int(input())
        k=0
        for i in range(0,j):
            print("ENTER NUMBER")
            w=float(input())
            k=k+w
        print("FINAL SOLUTION IS",k)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break
    elif i==2:
        print("\nHOW MANY NUMBERS WOULD YOU LIKE TO MULTIPLY")
        j=int(input())
        k=1
        for i in range(0,j):
            print("ENTER NUMBER")
            w=float(input())
            k=w*k
        print("FINAL SOLUTION IS",k)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
    elif i==3:
        print("ENTER DIVIDEND")
        j=float(input())
        print("ENTER DIVISOR")
        k=float(input())
        w=j/k
        print("FINAL SOLUTION IS",w)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
    elif i==4:
        print("ENTER FIRST NUMBER")
        j=float(input())
        print("ENTER SECOND NUMBER")
        k=float(input())
        print("FINAL SOLUTION IS",j-k)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
    elif i==5:
        print("CHOSSE WHICH OF THE FOLLOWING WOULD YOU LIKE TO PERFORM GIVEN ''INPUT MUST BE IN DEGREE''\n 1. SINE  2. COSINE\n 3. TANGENT  4. COTANGENT\n 5. SECANT  6. COSECANT")
        j=int(input())
        if j==1:
            print("ENTER NUMBER")
            k=float(input())
            print("RESULT IS",math.sin(math.radians(k)))
        elif j==2:
            print("ENTER NUMBER")
            k=float(input())
            print("RESULT IS",math.cos(math.radians(k)))
        elif j==3:
            print("ENTER NUMBER")
            k=float(input())
            print("RESULT IS",math.tan(math.radians(k)))
        elif j==4:
            print("ENTER NUMBER")
            k=float(input())
            print("RESULT IS",1/math.tan(math.radians(k)))
        elif j==5:
            print("ENTER NUMBER")
            k=float(input())
            print("RESULT IS",1/math.cos(math.radians(k)))
        if j==6:
            print("ENTER NUMBER")
            k=float(input())
            print("RESULT IS",1/math.sin(math.radians(k)))
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
    elif i==6:
        print("ENTER YOUR RADIAN(S)")
        j=float(input())
        print("IN DEGREE IT IS",j*57.2958)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
    elif i==7:
        print("ENTER YOUR NUMBER")
        j=float(input())
        print("ROOT OF",j,"IS",math.sqrt(j))
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
    elif i==8:
        print("ENTER YOUR NUMBER")
        j=float(input())
        print("SOLUTION IS",j*j*j)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
        
    elif i==9:
        print("ENTER NUMBER")
        j=float(input())
        print("RESULT IS",j*j)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break  
    elif i==10:
        print("ENTER x ")
        j=float(input())
        print("ENTER BASE VALUE i.e a")
        k=float(input())
        print("LOG VALUE IS ",math.log(j,k))
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break
    elif i==11:
        print("ENTER THE VALUE OF n")
        n=int(input())
        k=1
        for z in range(1,n+1):
         k=k*z
        print("ENTER THE VALUE OF r")
        r=int(input())
        y=1
        for z in range(1,r+1):
         y=y*z
        a=n-r
        w=1
        for z in range (1,n-r+1):
         w=w*z
        print("REQUIRED nCr is"k/(y*w))
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break
    elif i==12:
        print("ENTER THE VALUE OF n")
        n=int(input())
        print("ENTER VALUE OF r")
        r=int(input())
        a=n-r
        k=1
        w=1
        for i in range(1,n+1):
            k=k*i
        for i in range(1,n-r+1):
            w=w*i
        print("FINAL SOLUTION OF PERMUTATION IS",k/w)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break
    elif i==13:
        print("ENTER YOU NUMBER")
        j=int(input())
        k=1
        for i in range(1,j+1):
            k=k*i
        print("FACTORIAL IS",k)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break
    elif i==14:
        print("ENTER VALUE OF x")
        x=float(input())
        print("PROVIDE THE VALUE OF y")
        y=int(input())
        z=x
        for i in range(1,y):
            x=x*z
        print("SOLUTION IS",x)
        print("WOULD YOU LIKE TO PERFORM MORE CALCULATION\n YES   NO")
        q= input()
        if q=="yes" or q=="YES":
            continue
        else:
            break
        
        
        
        
        
        