def main():
      sum = 0
      num = int(input('enter a positive number (negative to end):'))
      
      while True:
          
          print(num)

          if num < 0:
              break
        



          sum = sum + num
          num = int(input('enter a positive number (negative to end):'))

      print('the sum of the numbers is:', sum)

main() 