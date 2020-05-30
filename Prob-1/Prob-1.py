# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Matthew Bly

def main():
    sum = 0
    number = int(input("Enter a number (negative to quit) >> "))
    while number >= 0:
        sum = sum + number
        number = int(input("Enter a number (negative to quit) >> "))
        
    print("the sum of the numbers are:", sum)
    
main()    