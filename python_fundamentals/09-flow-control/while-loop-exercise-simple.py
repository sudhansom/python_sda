while True:
    user_input = input("Enter something: ")
    if user_input == "exit":
        print(f"you entered {user_input}")
        print("Done...")
        break
    elif user_input == "exit-no-print":
        break
    elif user_input == "no-print":
        continue
    else:
        print(user_input)
