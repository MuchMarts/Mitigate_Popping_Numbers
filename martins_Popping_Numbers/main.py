from game import Game

def pick_size():
    while True:
        print("Choose Game size! (min 5, max 25)")
        choice = input("Enter choice: ")
        if int(choice) < 5 or int(choice) > 25:
            print("Invalid value. Try again!")
        else:
            return int(choice)

def choose_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    chosen = []
    while True:
        print("Select numbers to play with!")
        line = ''
        for num in numbers:
            if num not in chosen:
                line += ' ' + str(num) + ' '
            else:
                line += '[' + str(num) + ']'
        print(line)
        print("Choose number: [0-9]")
        print("Confirm choice: y")
        choice = input("Choice: ")
        if choice == 'y':
            return chosen
        if int(choice) in numbers and int(choice) not in chosen:
            chosen.append(int(choice))
        elif int(choice) in numbers and int(choice) in chosen:
            chosen.remove(int(choice))

while True:
    print("Welcome to the game: Popping Number!")
    print("Options")
    print("Start game [1]")
    print("Exit [any]")

    choice = input("Enter choice: ")

    if choice != "1":
        print("Thank you for playinig")
        break

    print('\n' * 100)

    size = pick_size()
    chosen = choose_numbers()

    game = Game(size, chosen)
    game.run()