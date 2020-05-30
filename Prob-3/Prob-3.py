# Module 7
#   Programming Assignment 10
#     Prob-3.py

# Matthew Bly

def main():
    sum = 0
    num = int(input('enter a positive number (negative to end):'))

    # do not change the while loop definition below
    while True:
        print(num)
        if num <= 0:
              break
        sum = sum + num
        num = int(input('enter a positive number (negative to end):'))

    print('the sum of the numbers is:', sum)

main()    