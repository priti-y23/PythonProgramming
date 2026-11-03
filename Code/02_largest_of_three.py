def largest_of_three(a, b, c):
    if a>=b and a>=c :
        return a
    elif b>=a and b>=c:
        return b 
    else :
        return c 


if __name__ == "__main__":
    a= int (input ("enter first number :"))
    b= int (input("enter second number :"))
    c= int (input("enter third number :"))
    print("Largest:", largest_of_three(a, b, c))