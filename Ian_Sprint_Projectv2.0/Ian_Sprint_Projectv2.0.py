try:
    input('What is ur age?: ') 
    print()  
    dog = input('Please enter your age?: ')
    print(f'{dog}?! that is a great age to be!')

    dog = int(input('What is ur age?: '))
    print(f'{dog}?! That is a great age to be!')
except ValueError:
    ptint('Error: That is not a valid number')
