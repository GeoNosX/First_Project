
def fizz_buzz(x):
        if x % 3==0 and not x%5==0:
            return("Fizz")
        elif x % 5==0 and not x % 3==0:
            return("Buzz")
        elif x % 3==0 and x%5==0:
             return("Fizz_Buzz")
        else:
             return(x)
        
print(fizz_buzz(15))