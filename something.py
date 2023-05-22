total = 0

number = int(input('Enter a number: '))

while number != 0:
    total += number    # total = total + number

    number = int(input('Enter a number: '))


print('total =', total)