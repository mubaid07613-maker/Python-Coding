print('So this program is basically a calculator')
while True:
    print("""1--> Addition\n2--> Multiplication\n3--> Subtraction\n4--> Division\n5--> Exit""")
    choice = int (input("Enter your choice: "))
    match choice:
        case 1:
            user_input = input ("So you have addition huh? noice! Enter your numbers: ")
            numbers = [int(x) for x in user_input.split(',')]
            print ("The sum is :", sum(numbers))
        case 2:
            product = 1  
            user_input = input ("So you have multiplication huh? noice! Enter your numbers: ")
            numbers = [int(x) for x in user_input.split(',')]
            for number in numbers:
                product = product * number
            print ("The product is :", product)
        case 3:
            user_input = input ("So you have subtraction huh? noice! Enter your numbers: ")
            numbers = [int(x) for x in user_input.split(',')]
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            print ("The answer is :", result)
        case 4:
            user_input = input ("So you have division huh? noice! Enter your numbers: ")
            numbers = [int(x) for x in user_input.split(',')]
            if 0 in numbers[1:]:
                print("You cant divide by zero!")
            else:
                result = numbers[0]
                for num in numbers[1:]:
                    result/=num
                print ("The result is :", result)
        case 5:
            print("Thanks for using this program!")
            break
        case _:
            print("You didnt enter correct choice")




