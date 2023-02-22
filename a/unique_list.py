# Accepts a series of inputted positive numbers and prints whether those numbers are unique

def main():
    print('This program tests if a sequence of inputted positive numbers are unique\n')
    input_num = int(input('Enter a number (-1 to quit): '))
    
    inputted_nums = []
    while input_num >= 0:
        inputted_nums.append(input_num)
        input_num = int(input('Enter a number (-1 to quit): '))
    
    unique = True
    for num in inputted_nums:
        if inputted_nums.count(num) > 1:
            unique = False
            break
    
    if unique:
        print(f'\nThe sequence {inputted_nums} is unique!')
    else:
        print(f'\nThe sequence {inputted_nums} is NOT unique!')

main()