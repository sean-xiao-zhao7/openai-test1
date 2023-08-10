def regular_attack():
    print("You perform a regular attack!")


def heavy_attack():
    print("You unleash a heavy attack!")


def heal_self():
    print("You heal yourself!")


def main():
    print("Welcome to the battle!")

    while True:
        print("Commands:")
        print("1. Regular Attack (ra)")
        print("2. Heavy Attack (ha)")
        print("3. Heal Self (h)")
        print("4. Quit (q)")

        user_input = input("Enter a command: ")

        if user_input == 'ra':
            regular_attack()
        elif user_input == 'ha':
            heavy_attack()
        elif user_input == 'h':
            heal_self()
        elif user_input == 'q':
            print("Quitting the battle.")
            break
        else:
            print("Invalid command. Please choose a valid option.")


if __name__ == "__main__":
    main()
