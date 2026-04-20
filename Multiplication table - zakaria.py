def multiplication_table():
    # ask the user to enter a number
    number = int(input("Enter a number: "))
    
    # print the title
    print(f"\nTable of ({number})")
    
    # loop from 1 to 10
    for b in range(1, 11):
        # print multiplication result
        print(f"{b}) {number} * {b} = {number*b}")

# call the function
multiplication_table()