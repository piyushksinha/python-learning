while True : 
    print("======================")
    print("1. Show Even Numbers")
    print("2. Show Squares")
    print("3. Reverse Names")
    print("4. Exit")
    print("======================")

    choice = int(input("Enter your choice: "))

    match choice : 
        case 1 :
            evens = [num for num in range(10) if num%2 == 0]
            print(evens)
        case 2 :
            squares = [i*i for i in range(5)] 
            print(squares)
        case 3: 
            name = input("Enter a name: ")
            print(f"Reversed Name: {name[::-1]}")
        case 4:
            break
        case _:
            print("Invalid Choice")