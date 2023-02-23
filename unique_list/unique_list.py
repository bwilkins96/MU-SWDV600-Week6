# Accepts a series of inputted positive numbers and prints whether those numbers are unique

def main():
    # Intro message and initial user input
    print('This program tests if a sequence of inputted positive numbers are unique\n')
    input_num = int(input('Enter a number (negative to quit): '))

    # Prompts user for positive numbers and appends them to a sequence
    # Inputting a negative number stops the loop    
    inputted_nums = []
    while input_num >= 0:
        inputted_nums.append(input_num)
        input_num = int(input('Enter a number (negative to quit): '))
    
    if len(inputted_nums) == 0:
        print('\nNo positive numbers were entered!')
        return
    
    # Iterate through inputted nums and check if count of any value is greater than 1
    unique = True
    for num in inputted_nums:
        if inputted_nums.count(num) > 1:
            unique = False
            break
    
    # Prints whether inputted nums is unique
    if unique:
        print(f'\nThe sequence {inputted_nums} is unique!')
    else:
        print(f'\nThe sequence {inputted_nums} is NOT unique!')

main()