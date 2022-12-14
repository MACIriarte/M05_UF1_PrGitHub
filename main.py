from function_1 import DeleteVowels as Exercise2
from function_2 import DeleteConsonants as Exercise3
from function_3 import BackwardPhrase as Exercise4
from function_4 import OrderPhrase as Exercise5

menu = "\n"+"*"*45+"\n1)Introduce the phrase\n2)Show the phrase given without vowels\n" \
              "3)Show the phrase given without consonants\n4)Show the phrase given backwards\n" \
              "5)Show the phrase given ordered\n6)Exit\n"+"*"*45
warning = "You need to introduce a phrase first!\n"
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
            phrase = input("\nPhrase: ")
        if option == 2:
            # Show the phrase given without vowels / Exercise 2
            while phrase == "":
                print(warning+menu)
                option = input("Option: ")

            print(Exercise2(phrase))
        if option == 3:
            # Show the phrase given without consonants / Exercise 3
            while phrase == "":
                print(warning+menu)
                option = input("Option: ")

            print(Exercise3(phrase))
        if option == 4:
            # Show the phrase given backwards / Exercise 4
            while phrase == "":
                print(warning+menu)
                option = input("Option: ")

            print(Exercise4(phrase))
        if option == 5:
            # Show the phrase given ordered / Exercise 5
            while phrase == "":
                print(warning+menu)
                option = input("Option: ")

            print(Exercise5(phrase))
        if option == 6:
            end = True
