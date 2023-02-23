# Accepts a series of inputs and prints whether those inputs are unique

def main():
    # Intro message
    print('This program tests if a sequence of inputs are unique\n')

    # Prompts user for inputs and appends them to a sequence
    # Pressing <enter> breaks out of the loop    
    inputs = []
    while True:
        input_val = (input('Enter a value (<enter> to quit): '))
        if input_val == '': break
        inputs.append(input_val)

    if len(inputs) == 0:
        print('\nNo values were entered!')
        return
    
    # Iterate through inputted values and check if count of any value is greater than 1
    unique = True
    for val in inputs:
        if inputs.count(val) > 1:
            unique = False
            break
    
    # Prints whether inputted values are unique
    if unique:
        print(f'\nThe sequence {inputs} is unique!')
    else:
        print(f'\nThe sequence {inputs} is NOT unique!')

main()