menu = ""
phrase = ""
input("\nPress any key to start the program")
end = False
while not end:
    print(menu)
    option = input("Option: ")
    if not option.isdigit():
        print("Only numbers!\n")
    elif int(option) not in range(1, 7):
        print("Option not complemented\n")
    else:
        option = int(option)
        if option == 1:
            # Introduce the phrase / Exercise 1
        if option == 2:
            # Show the phrase given without vowels / Exercise 2
        if option == 3:
            # Show the phrase given without consonants / Exercise 3
        if option == 4:
            # Show the phrase given backwards / Exercise 4
        if option == 5:
            # Show the phrase given ordered / Exercise 5
        if option == 6:
            end = True
