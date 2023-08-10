import random


def regular_attack():
    damage = random.randint(8, 12)
    print("You perform a regular attack and deal", damage, "damage!")
    return damage


def heavy_attack():
    damage = random.randint(16, 24)
    print("You unleash a heavy attack and deal", damage, "damage!")
    return damage


def heal_self():
    healing = random.randint(10, 20)
    print("You heal yourself for", healing, "HP!")
    return healing


def main():
    player_hp = 100
    enemy_hp = 100

    print("Welcome to the battle!")

    while True:
        print("\nPlayer HP:", player_hp)
        print("Enemy HP:", enemy_hp)

        print("Commands:")
        print("1. Regular Attack (ra)")
        print("2. Heavy Attack (ha)")
        print("3. Heal Self (h)")
        print("4. Quit (q)")

        user_input = input("Enter a command: ")

        if user_input == 'ra':
            damage = regular_attack()
            enemy_hp = max(0, enemy_hp - damage)
        elif user_input == 'ha':
            damage = heavy_attack()
            enemy_hp = max(0, enemy_hp - damage)
        elif user_input == 'h':
            healing = heal_self()
            player_hp = min(100, player_hp + healing)
        elif user_input == 'q':
            print("Quitting the battle.")
            break
        else:
            print("Invalid command. Please choose a valid option.")

        if enemy_hp <= 0:
            print("You defeated the enemy!")
            break

        if player_hp <= 0:
            print("You were defeated by the enemy!")
            break


if __name__ == "__main__":
    main()
