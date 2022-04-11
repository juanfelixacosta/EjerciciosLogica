# Algorithm that prints the numbers from zero (0) to one hundred (100), places the number that is even the word 'buzz'
# and the number that is a multiple of five (5) places 'bazz'

for num in range(0, 101):
    if num == 0:
        print(num)
    elif num % 2 == 0:
        print(num, 'buzz')
    elif num % 5 == 0:
        print(num, 'bazz')
    else:
        print(num)
